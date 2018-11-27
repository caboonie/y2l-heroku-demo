from flask import Flask, request, url_for, redirect
from flask import render_template
#from database import get_all_cats, get_cat, create_cat, update_vote
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("test.html")

@app.route('/add', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        pass
        #create_cat(request.form['cat_name'])
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
