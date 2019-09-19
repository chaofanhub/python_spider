'''
爬取CSDN指定博主的部分文章并保存为md格式

'''
#导入包
import requests
from parsel import Selector
from tomd import Tomd#保存为md文件
import re

#获取列表页中每一篇blog的url
def getArticleUrl(indexUrl):
    '''
    indexUrl:列表页url
    return:列表页中每一篇blog的url，返回列表
    '''
    try:
        r = requests.get(indexUrl)#发送请求
        r.raise_for_status()#获取网页状态
        #初始化生成一个XPath解析对象
        selectors = Selector(r.text)
        #使用XPath选取每一篇blog的url，返回列表
        article_urls = selectors.xpath('//div[@class="article-list"]//h4/a/@href').getall()
        return article_urls
    except:
        return '爬取articleUrl异常'

#获取blog的内容
def getOneArticle(article_url):
    '''
    article_url:blog的url
    提取数据，保存为md文件
    '''
    try:
        r = requests.get(article_url)#发送请求
        r.raise_for_status()#获取网页状态
        #初始化生成一个XPath解析对象
        selectors = Selector(r.text)
        #使用XPath选取每一篇blog的标题、内容，返回列表
        title = selectors.xpath('//h1[@class="title-article"]/text()').get()
        content = selectors.xpath('//article').get()
        #内容转换为md格式
        text = Tomd(content).markdown
        #使用空字符串替换不要的内容
        text = re.sub('<a.*?a>', '', text)
        print(title)
        #保存文件
        with open(title+'.md', 'w', encoding='utf-8') as f:
            f.write('#' + title)
            f.write(text)
    except:
        return "获取网页异常"

if __name__ == "__main__":
    userName = 'fei347795790'#博主名字
    depth = 1#爬取网页页数
    for i in range(depth):
        try:
            #CSDN blog列表页网址
            indexUrl = f'https://blog.csdn.net/{userName}/article/list/{i+1}?'
            article_urls = getArticleUrl(indexUrl)
            for article_url in article_urls:#遍历每一个url
                getOneArticle(article_url)
        except:
            continue









