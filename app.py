# -*-coding:utf-8-*-
from flask import Flask, make_response, url_for
from flask import request
from flask import Response
from flask import send_file
from flask import render_template

app = Flask(__name__, static_url_path='')


# css静态资源必须放到static目录下
@app.route('/404', methods=['GET', 'POST'])
def handle404():
    return app.send_static_file('html/404.html')


@app.errorhandler(404)
def not_found(error):
    return app.send_static_file('html/404.html')


@app.route('/', methods=['GET', 'POST'])
def hello():
    print(request.cookies)
    if request.method == 'GET':
        print(request.method, request.args)

    elif request.method == 'POST':
        print(request.method, request.form)
    return "hello 典!"


@app.route('/user/<name>', methods=['GET', 'POST'])
def index(name):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10708)
