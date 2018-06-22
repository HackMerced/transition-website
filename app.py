# do all the work here
from flask import Flask, render_template
import os
import inspect
import json
import threading
import urllib.request

app = Flask(__name__)

# get directory
filename = inspect.getframeinfo(inspect.currentframe()).filename
os.chdir(os.path.dirname(os.path.abspath(filename)))
path = os.path.abspath(os.curdir)

WEBSITE_URL = 'https://transition-website.herokuapp.com/'
SECONDS_IN_29_MIN = 1740


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def keep_server_awake():
    urllib.request.urlopen(WEBSITE_URL)


@app.route('/')
def index():
    return render_template('general/index.html')


@app.route('/join')
def jobs():
    positions = open(path + "/static/jobs.json", "r").read()
    positions = json.loads(positions)
    return render_template('general/join.html', jobs=positions)


#hello
if __name__ == "__main__":
    # want to ping itself every 29 minutes to prevent from sleeping
    set_interval(keep_server_awake, SECONDS_IN_29_MIN)
    app.run()
