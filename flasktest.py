from flask import Flask, render_template
import urllib3
import json

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
http = urllib3.PoolManager()

app = Flask(__name__)

def get_meme():
    response = http.request('GET', 'https://www.reddit.com/r/memes/random.api', headers={'User-agent':useragent} )
    data = json.loads(response.data)
    title = data[0]['data']['children'][0]['data']['title']
    pic = data[0]['data']['children'][0]['data']['url']
    return title, pic

@app.route("/")
def index():
    meme_title, meme_pic = get_meme()
    return render_template("index.html", meme_title=meme_title, meme_pic=meme_pic)

app.run(host="127.0.0.1", port=8080)