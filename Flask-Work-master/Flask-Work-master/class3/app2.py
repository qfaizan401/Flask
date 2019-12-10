from flask import Flask,redirect,render_template,request
app = Flask(__name__)


@app.route('/')
def l():
    return render_template('aaa.html')
@app.route('/home')
def home():
    return "Hello from Home Page"
@app.route('/login')
def login():
    return render_template('aaa.html')

app.run(debug=True)