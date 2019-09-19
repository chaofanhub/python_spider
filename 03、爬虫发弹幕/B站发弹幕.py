'''
B站发弹幕
'''
import requests
#替换请求头，反爬
data = {
    'type': '1',
    'oid': '80640052',
    'msg': '9999',
    'aid': '46026556',
    'progress': '3309',
    'color': '16777215',
    'fontsize': '25',
    'pool': '0',
    'mode': '1',
    'rnd': '1567910861745856',
    'plat': '1',
    'csrf': 'c722afb27afd90be0184368f3e71d763',      
    }

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av46026556/?p=7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', 
    "Cookie": "XXXXXXXXXXXXXXXXXX"
    }

#发弹幕
def main():  
    try:
        depth = 3#发弹幕次数
        url = "https://api.bilibili.com/x/v2/dm/post"#发弹幕地址
        for i in range(depth):
            message = str(input("请输入您要发送的弹幕："))#弹幕内容
            data['msg'] = message
            requests.post(url, data=data, headers=headers)
    except:
        return "发送失败"
main()   
    