from flask import Flask, render_template, url_for, redirect
from hoverpi import cmd, cmd_on, cmd_off
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', id=randint(0,65535))

@app.route('/touch')
def touch():
    return render_template('touch.html')

@app.route('/on/')
def on():
    cmd_on()
    return render_template('index.html', id=randint(0,65535))

@app.route('/off/')
def off():
    cmd_off()
    return render_template('index.html', id=randint(0,65535))

@app.route('/left/')
def left():
    cmd('l 4')
    return render_template('index.html', id=randint(0,65535))

@app.route('/right/')
def right():
    cmd('r 6')
    return render_template('index.html', id=randint(0,65535))

@app.route('/forward/')
def forward():
    cmd('f 10')
    return render_template('index.html', id=randint(0,65535))

@app.route('/reverse/')
def reverse():
    cmd('b 5')
    return render_template('index.html', id=randint(0,65535))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
