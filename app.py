#!/usr/bin/env python3
""" A basic flask app to serve the app"""


from flask import (Flask,request, abort, redirect, render_template, g, session, request, Blueprint, url_for)
from pyshorteners import Shortener

app = Flask(__name__)

@app.errorhandler(404)
def err404(e):
    return '<center><h1>4o4</h1><br/><h2> Not Found </h2></center>'

@app.route('/', strict_slashes=True)
def home():
    return render_template('index.htm')

@app.route('/shorten', strict_slashes=True, methods=['POST', 'GET'])
def shorten():
    if request.method == 'POST':
        try:
            url = request.form.get('url')
            short = Shortener() 
            url = short.dagd.short(url)
            return render_template('index.htm', res=url)
        except Exception:
            return render_template('index.htm', err='Enter a valid Url')
    return render_template('index.htm')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
