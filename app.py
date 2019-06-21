from flask import Flask
from flask import render_template
from flask import jsonify

import os, logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(lineno)d %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/menu')
def menu():
    info = {'sessionId': 'd'}
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3234, debug=False)
