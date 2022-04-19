import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '테스트 메일입니다'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'dnwnd1019@gmail.com'

# 여러명에게 메일보낼떄
# msg['To'] = 'dnwnd1019@gmail.com, 등등'

msg.set_content('테스트 본문입니다')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)