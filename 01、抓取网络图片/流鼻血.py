'''
爬取图片 鼻血止不住了～
'''

#导入包
import requests
#图片网址
url = "https://i5.meizitu.net/2019/09/01a02.jpg"
#保存路径
path = url.split('/')[-1]
try:
    #这个请求头是关键，没有这个Referer，图片打不开
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'https://www.mzitu.com/201072/2'       
}
    r = requests.get(url, headers=headers)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print("文件保存成功")
except:
    print("爬取失败")




