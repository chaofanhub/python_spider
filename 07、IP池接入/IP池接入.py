'''
豆瓣接入IP池
'''
#导入包
import requests
#给网址加上代理IP
def getHTMLText(url, url2):
    try:
        r = requests.get(url, timeout=30)#获取代理ip
        #IP池
        proxy = {
            'http': f'{r.text}',
            'https': f'{r.text}'
        }
        # 加上IP代理
        re = requests.get(url2, proxies=proxy, timeout=30)
        re.raise_for_status()#获取网页状态
        re.encoding = re.apparent_encoding#更改网页编码
        return re.text
    except:
        return "爬取失败"
#处理网页信息
def parserPage(html):
    try:
        with open("豆瓣图书.txt", "a", encoding='utf-8') as f:
            f.write(html)
    except:
        return "代理失败"
    
def main():
    #获取代理IP的地址
    url = 'http://127.0.0.1:5010/get/'
    #需要代理IP的网址
    depth = 3#网页页数
    #通用地址
    url2_start = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start='
    for i in range(depth):#循环爬取网页
        try:
            url2 = url2_start + str(20*i) + '&type=T'
            html = getHTMLText(url, url2)
            parserPage(html)
        except:
            continue
    
main()
