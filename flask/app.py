import flask
from flask import Flask
import sys
from flask import escape   #这个可以用来转移返回值，这样会很安全（恶意用户将代码输入进来）
app = Flask(__name__)
Flask.env = 'development'
@app.route('/')
def hello():
    return 'hello'

##<img src="{{url_for('static',filename='lADPDiCpxRW-FmjNAojNAhw_540_648.jpg')}}"/>

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' %escape(name)
#Flask.run(app, host='0.0.0.0', port=12345)
@app.route('/tlz')
def tlz():
    return flask.render_template('tlz.html')
@app.route('/ylz')
def ylz():
    return flask.render_template('ylz.html')
@app.route('/szb')
def szb():
    return flask.render_template('szb.html')

flask.Flask.run(app, host='30.43.105.22', port=12345)  #默认是127 5000端口!