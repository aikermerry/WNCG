import urllib.request
import re
from urllib import request
from bs4 import BeautifulSoup

articleUrl="https://www.qiushibaike.com/textnew/page/%d" #文章地址
commentTurl="https://www.qiushibaike.com/article/%s"#评论地址
page=1

commentattrs="comment-block clearfix floor-%d"
#1.获取网页源码
def getContentOrComment(Url):
   # user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    #headers={'User Agent':user_agent}#浏览器信息，头部信息
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req=request.Request(url=Url,headers=headers)#用地址创建一个request对象
    response=urllib.request.urlopen(req)#打开网址
    content=response.read()#读成源代码
    return content
while True:
    enter=input("点击enter查看或者输入exit退出：")
    if enter=='exit':
        break
    Url = articleUrl % page
    print(Url)
    page+=1

    articlePage=getContentOrComment(Url)#调用获取网页源码，
    soupAricle =BeautifulSoup(articlePage,'html.parser')#创建对象，html.parser（解析方式）还有一种是lxml
    articFlood=1
    for string in soupAricle.find_all(attrs='article block untagged mb15'): #attrs表示属性
        commtenId=str(string.get('id').strip()[11:])
        print(articFlood,'.',string.find(attrs ='content').get_text().strip())
        articFlood+=1
        commentTurl1=commentTurl%commtenId
        commentPage=getContentOrComment(commentTurl1)
        soupComment = BeautifulSoup(commentPage, 'html.parser')
        sum=0
        for comment in soupComment.find_all(attrs='replay'):
            commitA=comment.find(attrs='userlogin')
            commitTitle=commitA.get('title')
            commentBody=comment.find(attrs='body')
            commentNext=commentBody.get_text()
            print("     %s"%commitTitle,sum,':',commentNext)
            sum+=1




