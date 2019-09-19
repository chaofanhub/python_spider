'''
模拟登录美食杰
'''
#导入包
import requests
#请求头
data = {
     'redirect': 'http://i.meishi.cc/',
     'username': '1912437315@qq.com',
     'password': 'XXXXXXXXXXXXX'   
    }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '75',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'i.meishi.cc',
    'Origin': 'https://i.meishi.cc',
    'Referer': 'https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',   
    }
#模拟登录
def signIn(url):
    try:
        #登录跳转
        r = requests.post(url, headers=headers, data=data)
        #保存跳转页面
        with open('美食杰.html', 'wb') as f:
            f.write(r.content)
    except:
        return ""

def main():
    #登录网址
    url = "https://i.meishi.cc/login.php"
    signIn(url)

main()
    




