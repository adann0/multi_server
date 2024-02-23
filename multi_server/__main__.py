#!/usr/bin/env python3

import os
import sys

from distutils.log import debug
from fileinput import filename
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    files = [path for path in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), path))]
    return render_template('index.html', files=files)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory(os.getcwd(), filename, as_attachment=True)

@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.exists("uploads"):
            os.mkdir("uploads")

        f.save(os.path.join("uploads", f.filename))
        return render_template("Acknowledgement.html", name=f.filename)   

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        port = 80
    else:
        try :
            port = int(sys.argv[-1])
        except ValueError:
            sys.exit("Bad port.")
    app.run(host='0.0.0.0', port=port, debug=True)
