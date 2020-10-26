from flask import Flask

app = Flask(__name__)

@app.route('/<name>')

def home():
    return "Welcome!"
    
def hello(name):
    return "Hello {}!".format(name)