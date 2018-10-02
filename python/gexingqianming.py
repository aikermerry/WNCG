from flask import Flask ,render_template,request
from requests import post
from bs4 import  BeautifulSoup

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])#如果不指定GET/POST就只能有GET访问
def index():
    if request.method =='GET':#如果请求是GET，那么就意味着直接访问
      return render_template('index.html')#将文件d读进来，在将文件交给浏览器
    elif request.method =='POST':
        word = request.form.get('word')
        sizes = request.form.get('sizes')
        fonts = request.form.get('fonts')
        fontcolor = request.form.get('fontcolor')
        data ={
            'word':word,
            'sizes':sizes,
            'fonts':fonts,
            'fontcolor':fontcolor,
              }
        html = post('http://www.uustv.com/', data=data).text

        dom = BeautifulSoup(html)
        img_url =dom.find_all('div','tu')[0].img['src']
        print(img_url)
        apath = 'http://www.uustv.com/'+img_url
        print(apath,sizes)
        return render_template('index.html',apath=apath)



if __name__ == '__main__':
    app.run(debug=True,port=80)
