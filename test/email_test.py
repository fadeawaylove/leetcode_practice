import smtplib
import requests
import datetime
import pytz
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

tz = pytz.timezone("Etc/GMT-8")

start_day = datetime.datetime(2020, 8, 30, tzinfo=tz)


def get_pic():
    resp = requests.get("http://open.iciba.com/dsapi/").json()
    return resp["content"], resp["fenxiang_img"]


def send_email():
    title, img_url = get_pic()

    sender = 'fade_away_will@163.com'
    my_pass = 'JXKKIUKWPFNLLBSL'
    receivers = ['2682372712@qq.com', '1032939141@qq.com']

    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header("狗瓜", 'utf8')
    msgRoot['To'] = Header("猪瓜", 'utf-8')
    msgRoot['Subject'] = Header(title, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    mail_msg = f"""
    <h1>吃药啦~ 老婆~</h1>
    <h3>{title}</h3>
    <img src="{img_url}" width="%60" height="%60">
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)
        smtpObj.login(sender, my_pass)
        smtpObj.sendmail(sender, receivers, msgRoot.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


# while True:
#     today = datetime.datetime.now(tz=tz)
#     days_delta = (today - start_day).days
#     flag = (days_delta % 28) < 21
#     print(today)
#     if flag and today.hour == 22 and today.minute == 0:
#         send_email()
#     time.sleep(19)


send_email()