from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    ApiKey = os.getenv('ApiKey')
    url ="https://newsapi.org/v2/top-headlines?country=in&ApiKey="+ApiKey
    r = requests.get(url).json()
    cases = {
        'articles' : r['articles']
    }
    return render_template("index.html",case = cases)

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0',port=5000)
