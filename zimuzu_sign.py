'''
Author: 清欢
Date: 2020-12-08 18:36:36
LastEditTime: 2020-12-09 11:15:02
LastEditors: Please set LastEditors
Description: 人人字幕组自动签到，可上传服务器配合crontab自动执行。 替换登录账号和密码。
'''
import requests
import time

DOMAIN = "http://www.rrys2020.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Referer": "http://www.rrys2020.com/user/login"
}
DATA = {
    "account": "登录账号",
    "password": "登录密码",
    "remember" : 1,
    "url_back" : DOMAIN + "/user/user"
}

client = requests.Session()

def login():
    client.post(url=DOMAIN + "/User/Login/ajaxLogin", data=DATA, headers=HEADERS)

def sign():
    client.get(url=DOMAIN + "/user/sign", headers=HEADERS)
    time.sleep(1)
    res = client.get(url=DOMAIN + "/user/login/getCurUserTopInfo", headers=HEADERS)
    print("今日人人钻为：" + res.json()["data"]["userinfo"]["point"])
    pass

if __name__ == "__main__":
    
    # login 
    login()
    time.sleep(1)
    # sign
    sign()
    pass
