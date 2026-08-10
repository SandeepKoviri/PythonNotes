
def otp_(otp):
    rem = 3
    while rem > 0:
        user_otp =int(input("Enter otp:"))
        if otp ==user_otp:
            return "otp_verified_successful"
        else:
            rem -= 1
            if rem > 0:
                print(f"Please Enter check otp {rem} attempts left")
            else:
                return "see you"

import smtplib
from email.message import EmailMessage
import random

otp = random.randint(1111,9999)
msg = EmailMessage()

sen_mail = "koviri.sandeep@gmail.com"
sen_password = "ubli vxer rsxf ifzb"

recipients = [
    'koviri.sandeep5@gmail.com'
]

msg["From"] = sen_mail
msg["To"] = recipients
msg["Subject"] = "OTP verification"

msg.set_content(f"""
Hello

your otp is: {otp}

Please do not share this OTP with anyone. 


Thank you.
""")

# Send email
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(sen_mail, sen_password)
s.send_message(msg)
s.quit()

print("Mail sent successfully")

print(otp_(otp))