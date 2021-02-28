from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def Home():
   return render_template('index.html')

@app.route('/hh99')
def hanghae99():
   return render_template('hanghae99.html')

@app.route('/hh99/recent')
def hanghae99Recent():
   return render_template('hanghae99Recent.html')

@app.route('/htmlCss')
def htmlCss():
   return render_template('htmlCss.html')

@app.route('/htmlCss/recent')
def htmlCssRecent():
   return render_template('htmlCssRecent.html')

@app.route('/javaScript')
def javaScript():
   return render_template('javaScript.html')

@app.route('/javaScript/recent')
def javaScriptRecent():
   return render_template('javaScriptRecent.html')

@app.route('/python')
def python():
   return render_template('python.html')

@app.route('/python/recent')
def pythonRecent():
   return render_template('pythonRecent.html')

@app.route('/algorithm')
def algorithm():
   return render_template('algorithm.html')

@app.route('/algorithm/recent')
def algorithmRecent():
   return render_template('algorithmRecent.html')

@app.route('/honeyTip')
def honeyTip():
   return render_template('honeyTip.html')

@app.route('/honeyTip/recent')
def honeyTipRecent():
   return render_template('honeyTipRecent.html')

@app.route('/rank_hanghae99', methods=['GET'])
def rankHangHae99():
    blogs = list(db.ShareLog_HangHae99.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/rank_htmlCss', methods=['GET'])
def rankHtmlCss():
    blogs = list(db.ShareLog_HtmlCss.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/rank_javaScript', methods=['GET'])
def rankJavaScript():
    blogs = list(db.ShareLog_JavaScript.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/rank_python', methods=['GET'])
def rankPython():
    blogs = list(db.ShareLog_Python.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/rank_algorithm', methods=['GET'])
def rankAlgorithm():
    blogs = list(db.ShareLog_Algorithm.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/rank_honeyTip', methods=['GET'])
def rankHoneyTip():
    blogs = list(db.ShareLog_HoneyTip.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/hanghae99', methods=['GET'])
def listingHangHae99():
    blogs = list(db.ShareLog_HangHae99.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/hanghae99/recent', methods=['GET'])
def listingHangHae99Recent():
    blogs = list(db.ShareLog_HangHae99_Recent.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/htmlCSS', methods=['GET'])
def listingHtmlCss():
    blogs = list(db.ShareLog_HtmlCss.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/htmlCSS/recent', methods=['GET'])
def listingHtmlCssRecent():
    blogs = list(db.ShareLog_HtmlCss_Recent.find({}, {'_id': False}))
    return jsonify({'all_blogs': blogs})

@app.route('/javaSCRIPT', methods=['GET'])
def listingJavaScript():
    blogs = list(db.ShareLog_JavaScript.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/javaSCRIPT/recent', methods=['GET'])
def listingJavaScriptRecent():
    blogs = list(db.ShareLog_JavaScript_Recent.find({}, {'_id': False}))
    return jsonify({'all_blogs': blogs})

@app.route('/Python', methods=['GET'])
def listingPython():
    blogs = list(db.ShareLog_Python.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/Python/recent', methods=['GET'])
def listingPythonRecent():
    blogs = list(db.ShareLog_Python_Recent.find({}, {'_id': False}))
    return jsonify({'all_blogs': blogs})

@app.route('/Algorithm', methods=['GET'])
def listingAlgorithm():
    blogs = list(db.ShareLog_Algorithm.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/Algorithm/recent', methods=['GET'])
def listingAlgorithmRecent():
    blogs = list(db.ShareLog_Algorithm_Recent.find({}, {'_id': False}))
    return jsonify({'all_blogs': blogs})

@app.route('/honeyTIP', methods=['GET'])
def listingHoneyTip():
    blogs = list(db.ShareLog_HoneyTip.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'all_blogs': blogs})

@app.route('/honeyTIP/recent', methods=['GET'])
def listingHoneyTipRecent():
    blogs = list(db.ShareLog_HoneyTip_Recent.find({}, {'_id': False}))
    return jsonify({'all_blogs': blogs})

## API 역할을 하는 부분

@app.route('/hanghae99', methods=['POST'])
def savingHangHae99():
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
    db.ShareLog_HangHae99.insert_one(doc)
    db.ShareLog_HangHae99_Recent.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})

@app.route('/htmlCSS', methods=['POST'])
def savingHtmlCss():
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
    db.ShareLog_HtmlCss_Recent.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})

@app.route('/javaSCRIPT', methods=['POST'])
def savingJavaScript():
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
    db.ShareLog_JavaScript.insert_one(doc)
    db.ShareLog_JavaScript_Recent.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})

@app.route('/Python', methods=['POST'])
def savingPython():
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
    db.ShareLog_Python.insert_one(doc)
    db.ShareLog_Python_Recent.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})

@app.route('/Algorithm', methods=['POST'])
def savingAlgorithm():
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
    db.ShareLog_Algorithm.insert_one(doc)
    db.ShareLog_Algorithm_Recent.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})

@app.route('/honeyTIP', methods=['POST'])
def savingHoneyTip():
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
    db.ShareLog_HoneyTip.insert_one(doc)
    db.ShareLog_HoneyTip_Recent.insert_one(doc)


    return jsonify({'msg':'저장이 완료되었습니다.'})

@app.route('/api/like/hanghae99', methods=['POST'])
def like_starHangHae99():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_HangHae99.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_HangHae99.update_one({'title': title_receive},{'$set':{'like': new_like}})
    db.ShareLog_HangHae99_Recent.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': 'like 연결되었습니다!'})

@app.route('/api/like/htmlCSS', methods=['POST'])
def like_starHtmlCss():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_HtmlCss.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_HtmlCss.update_one({'title': title_receive},{'$set':{'like': new_like}})
    db.ShareLog_HtmlCss_Recent.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': 'like 연결되었습니다!'})

@app.route('/api/like/javaSCRIPT', methods=['POST'])
def like_starJavaScript():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_JavaScript.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_JavaScript.update_one({'title': title_receive},{'$set':{'like': new_like}})
    db.ShareLog_JavaScript_Recent.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': 'like 연결되었습니다!'})

@app.route('/api/like/Python', methods=['POST'])
def like_starPython():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_Python.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_Python.update_one({'title': title_receive},{'$set':{'like': new_like}})
    db.ShareLog_Python_Recent.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': 'like 연결되었습니다!'})

@app.route('/api/like/Algorithm', methods=['POST'])
def like_starAlgorithm():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_Algorithm.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_Algorithm.update_one({'title': title_receive},{'$set':{'like': new_like}})
    db.ShareLog_Algorithm_Recent.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': 'like 연결되었습니다!'})

@app.route('/api/like/honeyTIP', methods=['POST'])
def like_starHoneyTip():
    title_receive = request.form['title_give']
    target_blog = db.ShareLog_HoneyTip.find_one({'title': title_receive})
    current_like = target_blog['like']
    new_like = current_like + 1
    db.ShareLog_HoneyTip.update_one({'title': title_receive},{'$set':{'like': new_like}})
    db.ShareLog_HoneyTip_Recent.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': 'like 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)