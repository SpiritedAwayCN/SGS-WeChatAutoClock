import requests

url = 'http://wx.sanguosha.com/api/clock/do'
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat'

with open('cookie.txt') as f:
    cookie = f.readline()

headers = {
    'User-Agent': ua,
    'cookie' : cookie
}

r = requests.post(url=url, headers=headers)

print(r.json())