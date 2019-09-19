'''
腾讯招聘数据获取
JSON get
'''
#导入包
import requests
import csv
#获取网页id
def getHTMLId(page):
    try:
        '''
        page:网页页码
        return:返回详情页id，一个生成器
        '''
        #url参数
        params = {
            'pageSize': '10',
            'language': 'zh-cn',
            'area': 'cn',
            'pageIndex': page
        }
        r = requests.get(url1, params=params)#发送请求
        PostIds = r.json()["Data"]["Posts"]#提取数据
        for PostId in PostIds:
            yield PostId#返回一个生成器
    except:
        return "获取异常"
#获取网页内容
def getHTMLText(i_d):
    try:
        '''
        i_d:详情页id
        return:详情页内容
        '''
        #url参数
        params = {
            'language': 'zh-cn',
            'postId': i_d['PostId']
        }
        r = requests.get(url2, params=params)#发送请求
        return r.json()
    except:
        return "获取网页异常"
#解析网页数据
def parsePage(postInfo):
    try:
        '''
        postInfo:详情页内容
        提取信息，保存到csv文件
        '''
        #职位名称
        postName = postInfo["Data"]["RecruitPostName"]
        #职位简介
        BGName = postInfo["Data"]["BGName"]
        #工作职责
        responsibility = postInfo["Data"]["Responsibility"]
        #工作要求
        requirement = postInfo["Data"]["Requirement"]
        #各项数据组成一个列表
        data = [postName,BGName,responsibility,requirement]
        #不加newline=''会出现空行
        with open('腾讯招聘.csv', 'a', encoding='utf-8', newline='') as f:
            csv.writer(f).writerow(data)
    except:
        return ""

if __name__ == "__main__":
    depth = 3#网页页数
    #腾讯招聘列表页网址
    url1 = 'https://careers.tencent.com/tencentcareer/api/post/Query'
    #腾讯招聘详情页网址
    url2 = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId'
    #表头
    with open('腾讯招聘.csv', 'a', encoding='utf-8', newline='') as f:
        #这种写入方式，当写入的对象中有逗号也没有关系
        csv.writer(f).writerow(['职位名字','职位简介','工作职责','工作要求'])
    for page in range(1, depth+1):
        try:
            PostId = getHTMLId(page)
            for i_d in PostId:
                postInfo = getHTMLText(i_d)
                parsePage(postInfo)
        except:
            continue
