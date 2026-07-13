import os
import tempfile
import markdown

from xhtml2pdf import pisa
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)



def save_markdown(content: str, filename: str = "notes.md"):

    supabase.storage.from_(BUCKET).upload(
        filename,
        content.encode("utf-8"),
        file_options={
            "content-type": "text/markdown",
            "upsert": "true"
        }
    )

    url = supabase.storage.from_(BUCKET).get_public_url(filename)

    return {
        "status": "success",
        "file": url
    }



def markdown_to_pdf(md_url: str):

    import requests

    response = requests.get(md_url)
    response.raise_for_status()

    md = response.text

    html = markdown.markdown(md)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pisa.CreatePDF(html, dest=tmp)

        tmp.flush()

        pdf_filename = os.path.basename(md_url).replace(".md", ".pdf")

        with open(tmp.name, "rb") as f:

            supabase.storage.from_(BUCKET).upload(
                pdf_filename,
                f,
                file_options={
                    "content-type": "application/pdf",
                    "upsert": "true"
                }
            )

    os.remove(tmp.name)

    pdf_url = supabase.storage.from_(BUCKET).get_public_url(pdf_filename)

    return {
        "status": "success",
        "pdf": pdf_url
    }