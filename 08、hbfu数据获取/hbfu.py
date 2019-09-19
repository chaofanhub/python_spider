'''
河北金融学院 数据获取
只要知道这是post方法，问题全解决了
'''
#导入包
import requests
import re
#获取网页id
def getHTMLId(url1, start):
    #form表单
    data = {
        'start': f'{start}',
        'limit': '20',
        'type': '1'       
    }
    try:
        r = requests.post(url1, data=data, verify=False)#发送请求
        pattern = re.compile(r'"id":(.*?),"title"')#正则规则
        newsIds = pattern.findall(r.text)#正则匹配newsId
        return newsIds
    except:
        return ""
#获取网页内容
def getHTMLText(url2, newsId):
    #form表单
    data = {
        'id': f'{newsId}'       
    }
    try:
        r = requests.post(url2, data=data, verify=False)#发送请求
        return r.text
    except:
        return ""
#解析网页数据
def parsePage(newsInfo):
    try:
        #新闻信息
        title = re.search(r'"title":"(.*?)"', newsInfo, re.S).group(1)
        #createDate = re.search(r'"createDate":"(.*?)"', newsInfo, re.S).group(0)
        source = re.search(r'"source":"(.*?)"', newsInfo, re.S).group(1)
        hit = re.search(r'"hit":(.*?),', newsInfo, re.S).group(1)
        #content = re.search(r'\">(.*?)<p', newsInfo, re.S).group(0)
        with open('hbfunews.csv', 'a') as f:
            f.write(f'{title},{source},{hit}\n')
    except:
        return ""

def main():
    depth = 3#网页页数
    #学校新闻汇总网址
    url1 = 'https://www.hbfu.edu.cn/news/queryListForPage'
    #单条新闻网址
    url2 = 'https://www.hbfu.edu.cn/news/findById'
    #表头
    with open('hbfunews.csv', 'a') as f:
        f.write('{},{},{}\n'.format('新闻标题', '来源', '点击量'))
    for i in range(depth):
        try:
            start = 20*i
            newsIds = getHTMLId(url1, start)
            for newsId in newsIds:
                newsInfo = getHTMLText(url2, newsId)
                parsePage(newsInfo)
        except:
            continue

main()
