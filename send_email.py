
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '1373814735'
mail_pass = 'tvjilcigodlcbabf'

sender = '1373814735@qq.com'
receivers = ['1373814735@qq.com']

message = MIMEText('Pytho email text', 'plain', 'utf-8')
message['from'] = Header('Pan', 'utf-8')
message['to'] = Header('Test', 'utf-8')

message['Subject'] = Header('Python SMTP Email Test', 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    try:
        smtpObj.login(mail_user, mail_pass)
    except smtplib.SMTPException:
        print('登录失败')
        raise
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print('无法发送邮件')
    raise
