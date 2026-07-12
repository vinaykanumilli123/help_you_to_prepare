import os
from datetime import datetime
import markdown
import markdown
from xhtml2pdf import pisa

BASE_DIR = "storage/generated_files"




def save_markdown(content: str, filename: str = "notes.md"):
    """
    Save markdown content into a file.
    """

    os.makedirs(BASE_DIR, exist_ok=True)

    path = os.path.join(BASE_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return {
        "status": "success",
        "file": path
    }








def markdown_to_pdf(md_file: str):

    with open(md_file, "r", encoding="utf-8") as f:
        md = f.read()

    html = markdown.markdown(md)

    pdf_file = md_file.replace(".md", ".pdf")

    with open(pdf_file, "wb") as pdf:
        pisa.CreatePDF(html, dest=pdf)

    return {
        "status": "success",
        "pdf": pdf_file,
    }