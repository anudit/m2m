import requests
import bs4
from flask import Flask, render_template, request, redirect
import jinja2
import os
import markdown2
from MediumParser import parse

app = Flask(__name__)

@app.route('/')
def hello():
	return "hi"

@app.route('/read/<path:url>')
def convert(url):
    request = requests.get(url)
    if request.status_code == 200:
        title, author, data  = parse(url)
        data = markdown2.markdown(data)
        return render_template('index.html', ArticleTitle = title, ArticleAuthor = author, ArticleHTML = data)
    else:
        return "Invalid URL"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
