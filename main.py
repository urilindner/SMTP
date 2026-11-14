import smtplib
from email.message import EmailMessage

#המייל של אמא שלי, שלי היה תחת אבטחה מחמירה יותר כי שלי נחשב מייל של ילד

email_send = "taly.lindner@gmail.com"
my_password = "rfoy rxgw jjmk azee"
email_recv = "merrygeva312@gmail.com"
my_name = "אורי לינדנר"

msg = EmailMessage()

msg['Subject'] = f"שליחת SMTP מ- {my_name}"
msg['From'] = email_send
msg['To'] = email_recv
msg.set_content(f"{my_name}: \n !שלושה חברים עולים למונית אחרי בילוי, והנהג מבין שהם עייפים מאוד. הוא מתניע, מכבה מיד את המנוע ומכריז שהגיעו. הראשון יורד, השני משלם, והשלישי נותן לנהג סתירה וצועק עליו: פעם אחרונה שאתה נוסע כל כך מהר")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(email_send, my_password)
    server.send_message(msg)

print("sent!")