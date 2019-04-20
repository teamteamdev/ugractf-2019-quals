#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from datetime import datetime, timedelta
from flask import Flask, request, redirect

app = Flask(__name__)

SECRET_PATH = '/BDdCc5aA38eA2005Ac20cCB5bA4b4D8d'
SECRET_RESPONSE = 'ugra_ea5y_f4st_brutef0rce'

REDIRECT_LINK = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


@app.route('/favicon.ico')
def favicon():
    return "404", 404


@app.route(SECRET_PATH)
def get_flag():
    return SECRET_RESPONSE


@app.route('/')
def index():
    return app.send_static_file('book.html')


@app.route('/<unused>')
def rickroll(unused):
    return f'''<meta http-equiv="refresh" content="0;url='{REDIRECT_LINK}'" /><h1>Redirecting...</h1>'''


if __name__ == "__main__":
    app.run()

