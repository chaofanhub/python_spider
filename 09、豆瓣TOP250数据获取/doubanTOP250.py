'''
豆瓣电影TOP250 数据获取
get方法
'''
#导入包
import requests
import re
#获取网页id
def getHTMLId(url1):
    try:
        r = requests.get(url1)#发送请求
        pattern = re.compile(r'<a href="https://movie.douban.com/subject/(.*?)/" class="">')#正则规则
        movieIds = pattern.findall(r.text)#正则匹配newsId
        return movieIds
    except:
        return ""
#获取网页内容
def getHTMLText(url2):
    try:
        r = requests.get(url2)#发送请求
        r.raise_for_status()#获取网页状态
        r.encoding = r.apparent_encoding#更改网页编码
        return r.text
    except:
        return ""
#解析网页数据
def parsePage(movieInfo):
    try:
        #电影信息
        name = re.search(r'data-name="(.*?)"', movieInfo, re.S).group(1)
        img = re.search(r'data-image="(.*?)"', movieInfo, re.S).group(1)
        #summary = re.search(r'<span class="all hidden">(.*?)<br />', movieInfo, re.S).group(1)
        score = re.search(r'property="v:average">(.*?)</strong>', movieInfo, re.S).group(1)
        number = re.search(r'property="v:votes">(.*?)</span>', movieInfo, re.S).group(1)
        with open('doubanTOP250.csv', 'a', encoding='utf-8') as f:
            #f.write(f'{name},{img},{summary},{score},{number}\n')
            f.write(f'{name},{img},{score},{number}\n')
    except:
        return ""

def main():
    depth = 3#网页页数
    #电影汇总网址通用链接
    start_url1 = 'https://movie.douban.com/top250?start='
    #单部电影网址通用链接
    start_url2 = 'https://movie.douban.com/subject/'
    #表头
    with open('doubanTOP250.csv', 'a', encoding='utf-8') as f:
        f.write('{},{},{},{}\n'.format('电影名称', '电影图片', '电影评分', '评价人数'))
    for i in range(depth):
        try:
            url1 = start_url1 + str(25*i) + '&filter='
            movieIds = getHTMLId(url1)
            for movieId in movieIds:
                url2 = start_url2 + str(movieId) + '/'
                movieInfo = getHTMLText(url2)
                parsePage(movieInfo)
        except:
            continue

main()

















