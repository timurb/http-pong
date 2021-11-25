from flask import Flask
from flask import request
import os
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return str(request.headers) + "\n" + str(request.data) 

@app.route("/env")
def env():
    return str(json.dumps(dict(os.environ), indent=2))

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
