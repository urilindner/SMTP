import smtplib
import mimetypes
from email.message import EmailMessage

#המייל של אמא שלי, שלי היה תחת אבטחה מחמירה יותר כי שלי נחשב מייל של ילד

email_send = "taly.lindner@gmail.com"
my_password = "rfoy rxgw jjmk azee"
email_recv = "merrygeva312@gmail.com"
my_name = "אורי לינדנר"

msg = EmailMessage()
msg["Subject"] = f"שליחת SMTP מ- {my_name}"
msg["From"] = email_send
msg["To"] = email_recv
msg.set_content(f"{my_name}:\nמצורף קובץ למייל!")

# file path
file_path = "The Donkey’s Farmyard Complaint.png"

# find the tipe of of file
mime_type, _ = mimetypes.guess_type(file_path)
if mime_type is None:
    mime_type = "application/octet-stream"
maintype, subtype = mime_type.split("/", 1)

# file
with open(file_path, "rb") as file:
    msg.add_attachment(
        file.read(),
        maintype=maintype,
        subtype=subtype,
        filename=file_path
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(email_send, my_password)
    server.send_message(msg)

print("sent with attachment!")
