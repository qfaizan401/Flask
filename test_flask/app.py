from flask import Flask,redirect,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/login_page')
def login_page ():
    return render_template('login_page.html')

# @app.route('/login_page')
# def login_page ():
#     return redirect('/login_page')



app.run(debug=True)