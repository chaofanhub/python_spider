'''
豆瓣电影TOP250 数据获取
get方法
'''
#导入包
import requests
import csv
from parsel import Selector
#获取网页id
def getHTMLId(page):
    try:
        '''
        page:网页页码
        return:返回详情页id，一个列表
        '''
        #url参数
        params = {
            'start': f'{25*page}'
        }
        r = requests.get(url, params=params, timeout=30)#发送请求
        r.raise_for_status()#获取网页状态
        #初始化生成一个XPath解析对象
        selectors = Selector(r.text)
        #使用XPath选取指定内容，返回列表
        detail_urls = selectors.xpath('//div[@class="hd"]/a/@href').getall()#返回一个列表
        return list(set(detail_urls))#去重
    except:
        return ""
#获取网页内容
def getHTMLText(detail_url):
    try:
        '''
        detail_url:详情页网址
        return:详情页内容
        '''
        r = requests.get(detail_url)#发送请求
        r.raise_for_status()#获取网页状态
        return r.text
    except:
        return ""
#解析网页数据
def parsePage(movieInfo):
    try:
        '''
        movieInfo:详情页内容
        提取信息，保存到csv文件
        '''
        #初始化生成一个XPath解析对象
        selectors = Selector(movieInfo)
        #电影名称
        name = selectors.xpath('//div[@id="content"]/h1/span/text()').getall()
        name = ''.join(name)#字符串拼接
        #电影海报链接
        img = selectors.xpath('//div[@id="mainpic"]//img/@src').get()
        #电影评分
        score = selectors.xpath('//div[@id="interest_sectl"]//strong/text()').get()
        #评价人数
        ratingCount = selectors.xpath('//div[@class="rating_sum"]//span/text()').get()
        #电影简介
        summary = selectors.xpath('//span[@property="v:summary"]/text()').getall()
        if summary:#判断简介是否为空
            summary = ''.join(summary)#简介拼接
            summary = summary.strip()#去掉字符串前后不可见字符
        else:
            summary = ''
        #各项数据组成一个列表
        item = [name,img,score,ratingCount,summary]
        with open('doubanTOP250.csv', 'a', encoding='utf-8', newline='') as f:
            csv.writer(f).writerow(item)
    except:
        return ""

if __name__ == "__main__":
    depth = 1#网页页数
    #电影列表页网址
    url = 'https://movie.douban.com/top250'
    #表头
    with open('doubanTOP250.csv', 'a', encoding='utf-8', newline='') as f:
        csv.writer(f).writerow(['电影名称','电影图片','电影评分','评价人数','剧情简介'])
    for page in range(depth):
        try:
            detail_urls = getHTMLId(page)
            for detail_url in detail_urls:
                movieInfo = getHTMLText(detail_url)
                parsePage(movieInfo)
        except:
            continue


















