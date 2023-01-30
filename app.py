from flask import Flask,render_template,request,session,logging,url_for,redirect,flash,g
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=['GET','POST'])
def login():
    userName = ""
    password = ""
    error = None
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route("/signup",methods=['POST','GET'])
    firstName = ""
    lastName = ""
    email = ""
    password = ""
def signup():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template("signup.html")

@app.route("/home",methods=['POST','GET'])
def home():
    return render_template("home.html")


if __name__== "__main__":
    app.run(debug=True)