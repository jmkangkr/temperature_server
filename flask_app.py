from flask import Flask, render_template, request, redirect, url_for
import json
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'TEMPERATURE': 25.5, 'HUMIDITY': 0.65})


if __name__ == '__main__':
    print("============ " + str(datetime.datetime.now()))
    app.run(debug=True, host='0.0.0.0')
