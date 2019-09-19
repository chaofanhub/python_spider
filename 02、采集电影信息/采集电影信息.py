'''
第四题 采集电影信息 网址打不开，用了别的网站
'''

#导入模块
import requests
from bs4 import BeautifulSoup

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'   
}

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
def parsePage(html):
    try:
        soup = BeautifulSoup(html, "html.parser")#煲汤
        infos = soup.find('ul', {'class': 'tv-list clearfix'}).find_all('li')#返回一个列表
        with open(r'电影信息.csv', "a", encoding='utf-8') as f:
            for info in infos:
                title = info.find('p', {'class': 'v-tit'}).get_text()#遍历列表，提取字符串
                starrings = info.find('p', {'class': 's-des'}).get_text()
                #director = info.find('p', {'class': 's-des'}).get_text()#导演不会提取
                f.write('{},{}\n'.format(title, starrings))
    except:
        return "发生异常"

def main():
    depth = 5#爬取页面页数
    start_url = 'http://www.piaohuacc.com/type/1/'#通用链接
    for i in range(1, depth+1):#循环爬取网页
        try:
            url = start_url + str(i) + '.html'
            html = getHTMLText(url)
            parsePage(html)
        except:
            continue

main()