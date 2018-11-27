from flask import Flask, request, url_for, redirect
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)
