#!/usr/bin/env python3

import os
import subprocess
import tempfile

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=["POST"])
def validate():
    try:
        with tempfile.TemporaryDirectory() as d: 
            request.files["file"].save(d + '/docker-compose.yml')
            output = subprocess.run(["/bin/sh", "-c", "docker-compose config"], cwd=d,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = (output.returncode == 0)
    except:
        result = "Exception"
    return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(port=49800)

