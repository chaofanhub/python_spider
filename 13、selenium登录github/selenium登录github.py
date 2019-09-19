'''
使用selenium登陆Github 并且点赞
'''
import time
from selenium import webdriver

#用类来编写
class GithubLogin(object):
    #初始化
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        
    #模拟登录
    def signIn(self, userName, passWord):
        # 打开网址
        self.driver.get(self.url)
        
        #定位账号输入框的位置
        inputUserName = self.driver.find_element_by_xpath('//*[@id="login_field"]')
        #在账号输入框中输入账号
        inputUserName.send_keys(userName)
        time.sleep(1)
        
        #定位密码输入框的位置
        inputPassWord = self.driver.find_element_by_xpath('//*[@id="password"]')
        #在密码输入框中输入密码
        inputPassWord.send_keys(passWord)
        time.sleep(1)
        
        #点击sign in 定位点击位置
        clickSignIn = self.driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[7]')
        #点击
        clickSignIn.click()
        time.sleep(1)
        
        
        
    
    #搜索内容
    def searchArticle(self, title):
        #定位搜索框
        inputSearch = self.driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]')
        #输入搜索内容
        inputSearch.send_keys(title)
        time.sleep(1)
        
        #定位确认框
        clickSearch = self.driver.find_element_by_xpath('//*[@id="jump-to-suggestion-search-global"]/a/div[2]')
        #点击要搜索的内容
        clickSearch.click()
        time.sleep(1)
    
    #点击想要的文章 
    def getArticle(self):
        #定位找到的文章
        clickHub = self.driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[1]/h3/a')
        #点击进入
        clickHub.click()
        time.sleep(3)
        
    #对文章点赞
    def star(self):
        #定位点赞框
        clickStar = self.driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[1]/div/ul/li[3]')
        #点击
        clickStar.click()
        time.sleep(1)

if __name__ == '__main__':
    #变量
    url = 'https://github.com/login'
    title = 'chaofanhub/python-scrapy'
    userName = 'chaofanhub'
    passWord = 'XXXXXXXX'
    
    githubLogin = GithubLogin(url)#实例化类
    githubLogin.signIn(userName, passWord)#登录
    githubLogin.searchArticle(title)#搜索
    githubLogin.getArticle()#进入相关hub
    githubLogin.star()#点赞
    
    
    
    
    
    
    
    
    
    
    
    
    
    