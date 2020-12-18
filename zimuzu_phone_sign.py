'''
Author: your name
Date: 2020-12-10 10:43:24
LastEditTime: 2020-12-10 11:01:30
LastEditors: Please set LastEditors
Description: 手机端每日签到, 抓包获取uid和token
'''

import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import requests

UID = "终端uid"
TOKEN = "终端token"

LOGIN_URL = "http://h5.rrhuodong.com/index.php?g=api/mission&m=index&a=login&uid={}&token={}&app=3&client=7".format(UID, TOKEN)
SIGN_URL = "http://h5.rrhuodong.com/index.php?g=api/mission&m=clock&app=3&client=7&a=store&id=2"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Referer": "http://h5.rrhuodong.com/mobile/mission/pages/task.html"
}

session = requests.Session()


class Mail():

    def __init__(self, host, user, passwd):
        self.smtp = smtplib.SMTP_SSL(host, 465)
        self.user = user
        self.smtp.login(user, passwd)

    def send_mail(self, receivers, title, content):
        message = MIMEText(content, "plain", "utf-8")
        message["From"] = self.user
        message["To"] = receivers
        message["Subject"] = title
        try:
            self.smtp.sendmail(self.user, receivers, message.as_string())
        except Exception as e:
            print(e)



def login():
    res = session.get(url=LOGIN_URL, headers=HEADERS)
    print(res.json())
    return res.json()["status"]

def sign():
    res = session.get(url=SIGN_URL, headers=HEADERS)
    print(res.json()["info"])



if __name__ == "__main__":
    # login get session
    status_code = login()
    if status_code != 1:
        email = Mail("smtp.163.com", "邮箱账号", "邮箱密码")
        email.send_mail("接受邮箱账号", "人人字幕签到失败", "请及时更新token值")
    # sign in 
    sign()