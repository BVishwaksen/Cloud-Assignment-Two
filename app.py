from flask import Flask,render_template,request,session,logging,url_for,redirect,flash,g
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=['GET','POST'])
def login():
    return 'Hello World'

if __name__== "__main__":
    app.run(debug=True)