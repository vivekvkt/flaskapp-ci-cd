from flask import Flask
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is my first Docker learing application in flask.'

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8085)