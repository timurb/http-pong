from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return str(request.headers) + "\n" + str(request.data)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
