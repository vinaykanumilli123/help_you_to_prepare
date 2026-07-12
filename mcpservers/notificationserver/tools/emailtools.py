import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()


SMTP_SERVER = os.getenv(
    "SMTP_SERVER"
)

SMTP_PORT = int(
    os.getenv("SMTP_PORT")
)

EMAIL_USER = os.getenv(
    "EMAIL_USER"
)

EMAIL_PASSWORD = os.getenv(
    "EMAIL_PASSWORD"
)


def send_email(
        receiver: str,
        subject: str,
        message: str
):
    """
    Send a simple email notification.
    """

    email = EmailMessage()

    email["From"] = EMAIL_USER
    email["To"] = receiver
    email["Subject"] = subject

    email.set_content(message)


    try:

        with smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        ) as server:

            server.starttls()

            server.login(
                EMAIL_USER,
                EMAIL_PASSWORD
            )

            server.send_message(
                email
            )


        return {
            "status": "success",
            "message": "Email sent successfully"
        }


    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

def send_zip(
        receiver: str,
        file_path: str
):
    """
    Send study material ZIP file.
    """


    email = EmailMessage()

    email["From"] = EMAIL_USER
    email["To"] = receiver
    email["Subject"] = "Your Study Material"


    email.set_content(
        "Your generated notes are attached."
    )


    try:

        with open(
            file_path,
            "rb"
        ) as f:

            file_data = f.read()


        email.add_attachment(
            file_data,
            maintype="application",
            subtype="zip",
            filename=os.path.basename(file_path)
        )


        with smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        ) as server:

            server.starttls()

            server.login(
                EMAIL_USER,
                EMAIL_PASSWORD
            )

            server.send_message(
                email
            )


        return {
            "status":"success",
            "message":"ZIP sent successfully"
        }


    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }