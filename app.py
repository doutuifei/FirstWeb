# -*-coding:utf-8-*-
from flask import Flask
from flask import request
from flask import Response
from flask import send_file
from flask import render_template

app = Flask(__name__, static_url_path='')

# css静态资源必须放到static目录下
@app.route('/404', methods=['GET', 'POST'])
def handle404():
    return app.send_static_file('html/404.html')

@app.route('/')
def hello():
    return "hello!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10708)
