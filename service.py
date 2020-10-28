from flask import Flask
# This is a comment
app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return "Hello {}!".format(name)

def home():
    return "Welcome!"
    