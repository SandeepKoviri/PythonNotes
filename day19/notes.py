'''
smtplibeary
-----------------


import smtplib as sl
import random


sender_mail = 'koviri.sandeep@gmail.com'
sender_password = 'ubli vxer rsxf ifzb'
rev_mail = 'bunnyjanga.ai@gmail.com'
subject = 'send'
message = """
Hello!

bigggggggg fruit anna nuvuuu


thank you..

#using for more then one 
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
'''