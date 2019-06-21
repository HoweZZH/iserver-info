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
    xmlapi = 'Z:/BIN/x64/zihao_xmlapi.log'
    sessionId = None
    with open(xmlapi, 'r') as f:
        lines = f.readlines()
        print(lines[-3:])
        for line in lines[-10:]:
            idx = line.find('SID:')
            if idx != -1:
                sessionId = line[idx+4: idx+36]

    info = {'sessionId': sessionId}
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
