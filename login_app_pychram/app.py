from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://qfaizan401:ayf112bqp332@app-flask-getting-started-n8ir5.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/login')
def login ():
    return render_template('login_app.html')

@app.route('/loginAuth', methods = ['POST'])
def loginAuth ():
    data = dict(request.form)
    test_data = mongo.db.test_data
    test_data.insert_one(data)
    return redirect('/login')

app.run(debug=True,port=8080)