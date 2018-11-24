from flask import Flask, request, url_for, redirect
from flask import render_template
from database import get_all_cats, get_cat, create_cat, update_vote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
 
@app.route('/cats/<string:id>', methods=['GET', 'POST'])
def cat_page(id):
    if request.method == 'POST':
        update_vote(id)
    cat = get_cat(id)
    return render_template("cat.html", name=cat.name)

@app.route('/add', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        create_cat(request.form['cat_name'])
    return render_template("add.html")


if __name__ == '__main__':
   app.run(debug = True)
