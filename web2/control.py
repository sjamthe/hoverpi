from flask import Flask, jsonify, render_template, request, url_for, redirect
from hoverpi import hovercmd

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('control.html')

@app.route('/<any(on, off, forward, backward, left, right):arg>')
def cmd(arg):
    resp=hovercmd(arg)
    return jsonify(result=resp)
