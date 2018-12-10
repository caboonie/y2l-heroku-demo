from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("hello.html")

@app.route('/test')
def hello_world():
    return "Test Boi"

if __name__ == '__main__':
    app.run(debug=True)
