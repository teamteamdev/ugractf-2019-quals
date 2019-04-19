#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from datetime import datetime, timedelta
from flask import Flask, request, redirect
from functools import wraps
from pymongo import MongoClient, ReturnDocument

app = Flask(__name__)
client = MongoClient(os.environ["MONGODB_URI"])
db = client.cloudfleet

SECRET_PATH = '/Cb2F87Ed60a4d290E2DdB7ffDB77a2e5'
SECRET_RESPONSE = 'ugra_unb4n_my_1p_p13453'

REDIRECT_LINK = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


@app.route('/favicon.ico')
def favicon():
    return "404", 404


def cloudfleet(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "cloudfleet" not in request.headers.get("Host", None):
            return "Bad password", 401
        global db

        ip = request.headers.get("X-Real-IP", request.remote_addr)
    
        db.ips.find_one_and_update(
            {"ip": ip},
            {"$push": {"visits": datetime.now()}},
            upsert=True
        )

        record = db.ips.find_one_and_update(
            {"ip": ip},
            {"$pull": {"visits": {"$lte": datetime.now() - timedelta(seconds=10)}}},
            return_document=ReturnDocument.AFTER
        )

        if len(record["visits"]) >= 3:
            return "<h1>You were banned by CloudFleet®</h1><p>Your requests look like automatical. Try again in 10 seconds.</p>", 429
        else:
            return func(*args, **kwargs)
    return wrapper    


@app.route(SECRET_PATH)
@cloudfleet
def get_flag():
    return SECRET_RESPONSE


@app.route('/')
@cloudfleet
def index():
    return app.send_static_file('book.html')


@app.route('/<unused>')
@cloudfleet
def rickroll(unused):
    return f'''<meta http-equiv="refresh" content="0;url='{REDIRECT_LINK}'" /><h1>Redirecting...</h1>'''


if __name__ == "__main__":
    app.run()

