import urllib.request
from  urllib import  request
from bs4 import BeautifulSoup
import re
import time
import itchat
xiHua="http://www.xhu.edu.cn/18/list%d.htm"
commentUrl="http://www.xhu.edu.cn/c0/68/c18a114792/page.htm"
xiHuaPage=1
xihuaUrl=xiHua%xiHuaPage
commentSign = 0
scanNnmber = 1

itchat.auto_login(hotReload=True)
user=itchat.search_friends('艾克merry')[0]['UserName']

def getContentOrComment(Url):
    headers=headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req=request.Request(url=Url,headers=headers)
    response=urllib.request.urlopen(req).read()
    return response
print('运行中请不要关闭 .......')
while True:
    commentTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    commentDayTime = time.strftime('%H-%M-%S', time.localtime(time.time()))
    #if commentDayTime =='12-00-00'or commentDayTime=='17-00-30':
    commentSign = 1

    if commentSign == 1:
        print('采集次数:',scanNnmber)
        scanNnmber+=1
        articlePage=getContentOrComment(xihuaUrl)
        soupArticle=BeautifulSoup(articlePage,'html.parser')
        num=0
        for commentNewTitle in soupArticle.find_all(attrs='column-news-title'):
            commentTitle=commentNewTitle.get_text()
            if re.search(r'招标',commentTitle,re.M|re.I):
               #if commentTime==commentNewTitle.get_text():
                    print(commentTitle)
                    document = open(r"text.txt", "a")
                    document.write('%d.'%num)
                    document.write(commentTitle)
                    document.write("  %s"%commentTime)
                    document.write('\n')
                    document.close()
                    num+=1

            commentSign=0
            time.sleep(1)
    if num>=1:
        itchat.send_msg("text.txt", toUserName='filehelper')










