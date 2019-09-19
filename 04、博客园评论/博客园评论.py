'''
博客园自动评论器
'''
#导入包
import requests
import random
#请求头，这是以JSON形式提交数据
data = {
    'body': "写的很棒",
    'parentCommentId': '0',
    'postId': '11484259',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '61',
    'content-type': 'application/json; charset=UTF-8',
    'cookie': 'XXXXXXXXXXXXXX',
    'origin': 'https://www.cnblogs.com',
    'referer': 'https://www.cnblogs.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
# 传递JSON数据
#r = requests.post(url, data=json.dumps(data))
#自动发送评论
def sendComment(url):
    depth = 3#评论次数
    #评论列表
    commentList = ['666', '999', '不错', '优秀', 'Good', 'Nice', 'Useful']
    for i in range(depth):
        try:
            #data['body'] = str(input("请输入你的评论："))
            data['body'] = random.choice(commentList)#随机选取评论
            #传递JSON数据
            requests.post(url, json=data, headers=headers) 
        except:
            return ""

def main():
    # 评论网址    
    url = 'https://www.cnblogs.com/Summer-skr--blog/ajax/PostComment/Add.aspx'
    sendComment(url)

main()
