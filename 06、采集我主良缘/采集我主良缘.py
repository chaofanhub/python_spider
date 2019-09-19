'''
采集我主良缘图片(21～30妹子)链接
'''
#导入包，由于获得json数据所以要用到json包
import requests
import json
#获取网页信息
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)#发出请求获取网页
        r.raise_for_status()#获取网页状态
        return json.loads(r.text)#输出网页内容
    except:
        return "爬取失败"
#处理网页信息
def parserPage(html):
    try:
        listInfo = html["data"]["list"]#提取图片链接，构成一个列表
        with open("图片url.csv", "a", encoding='utf-8') as f:
            for info in listInfo:#遍历列表
                #图片链接是字典类型，获取字典值，保存在CSV文件中
                f.write('{}\n'.format(info['avatar']))
    except:
        return "发生异常"

def main():
    depth = 2#爬取网页页数
    #通用网址
    start_url = "http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&marry=1&page="
    for i in range(1, depth+1):
        try:
            url = start_url + str(i)#网址
            html = getHTMLText(url)
            parserPage(html)
        except:
            return "爬取失败1"

main()
