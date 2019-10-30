from flask import Flask, render_template


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/interests')
def interests():
    return render_template('interests.html')
