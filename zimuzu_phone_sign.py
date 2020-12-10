'''
Author: your name
Date: 2020-12-10 10:43:24
LastEditTime: 2020-12-10 11:01:30
LastEditors: Please set LastEditors
Description: 手机端每日签到, 抓包获取uid和token
'''

import time
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

def login():
    res = session.get(url=LOGIN_URL, headers=HEADERS)
    print(res.json())

def sign():
    res = session.get(url=SIGN_URL, headers=HEADERS)
    print(res.json()["info"])



if __name__ == "__main__":
    # login get session
    login()
    # sign in 
    sign()