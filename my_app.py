#!/usr/bin/env python3

import os

from flask import Flask
from flask import request
from loguru import logger

app = Flask(__name__)


@app.route("/")
def main_app():
    return f"<h1>Welcome to the Sample App - {request.remote_addr}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
