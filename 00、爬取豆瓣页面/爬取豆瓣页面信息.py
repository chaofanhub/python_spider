'''
第二题 爬取豆瓣页面信息
'''

#导入模块
import requests
#获取网页信息
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)#获取网页
        r.raise_for_status()#获取网页状态
        r.encoding = r.apparent_encoding#更改网页编码
        return r.text#输出网页内容
    except:
        return ""
#处理网页信息   
def parsePage(i, html):
    #网页信息保存路径
    path = '豆瓣页面信息' + str(i+1) + '.txt'
    try:
        with open(path, "a", encoding='utf-8') as f:
            f.write(html)#保存网页信息
    except:
        return "发生异常"

def main():
    depth = 5#爬取页面页数
    start_url = 'https://movie.douban.com/top250?start='#通用链接
    for i in range(depth):#循环爬取网页
        try:
            url = start_url + str(25*i) + '&filter='
            html = getHTMLText(url)
            parsePage(i, html)
        except:
            continue

main()


