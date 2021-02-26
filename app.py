from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    blogs = list(db.ShareLog_HtmlCss.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    # desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title':title,
        'image':image,
        'comment':comment_receive,
        'url': url_receive,
        'name': name_receive,
        'like': 0
    }
    db.ShareLog_HtmlCss.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})
@app.route('/api/like', methods=['POST'])
def like_star():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_HtmlCss.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_HtmlCss.update_one({'title': title_receive},{'$set':{'like': new_like}})


    return jsonify({'msg': 'like 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)