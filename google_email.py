import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.parser import Parser

email_file = './email.txt'
mail_usr = 'pan@borderxlab.com'
mail_pass = '<Jdxm1314>'
sender = ''
receivers = ['']
mail_sub = ''
mail_content = ''

with open(email_file) as fp:
    headers = Parser().parse(fp)
    sender = headers['From'] 
    receivers = headers['To'].split(',')
    mail_sub = headers['Subject']
    mail_content =  headers.get_payload()

message = MIMEText(mail_content, 'plain', 'utf-8')
message['From'] = Header('Pan', 'utf-8')
message['To'] = Header('all', 'utf-8')
message['Subject'] = Header(mail_sub, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login(mail_usr, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('Send Succeed')
except:
    print("Error: Send faild for:")
    raise
