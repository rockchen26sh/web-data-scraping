import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is my python SMTPLIB text Email")

msg['subject'] = 'An Email Alert'
msg['From'] = 'cck878@qq.com'
msg['To'] = "cck8787878@gmail.com"

s = smtplib.SMTP('smtp.qq.com')
s.send_message(msg)
s.quit()