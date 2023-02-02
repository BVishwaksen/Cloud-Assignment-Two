from flask import Flask,render_template,request,session,logging,url_for,redirect,flash,g
import sqlite3
import os


conn = sqlite3.connect('cloudassignment.db')
mycursor = conn.cursor()

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=['GET','POST'])
def login():
    userName = ""
    password = ""
    firstname = ""
    lastname = ""
    email = ""
    error = None
    if request.method == 'POST':
        conn = sqlite3.connect('cloudassignment.db')
        mycursor = conn.cursor()
        userName = request.form['userName']
        password = request.form['password']
        sql = "SELECT * FROM users WHERE username = ?"
        uname = [userName]
        mycursor.execute(sql,uname)
        myresult = mycursor.fetchall()
        if(len(myresult) == 0):
            error = "User Name does not exist"
            return render_template('login.html',error=error)
        pwd = myresult[0][4]
        if pwd != password:
            error = "Invalid Password"
            return render_template('login.html',error=error)
        return render_template('home.html',firstName=myresult[0][1],lastName=myresult[0][2],userEmail=myresult[0][3])
    return render_template('login.html',error=error)

@app.route("/signup",methods=['POST','GET'])
def signup():
    username = ""
    password = ""
    firstname = ""
    lastname = ""
    email = ""
    if request.method == 'POST':
        conn = sqlite3.connect('cloudassignment.db')
        mycursor = conn.cursor()

        username = request.form['userName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        email = request.form['userMail']
        password = request.form['password']
        sql = "INSERT INTO users (username, firstname, lastname, email, userpassword) VALUES (?, ?, ?, ?, ?)"
        val = (username,firstname,lastname,email,password)
        mycursor.execute(sql, val)
        conn.commit()
        return render_template('home.html',firstName=firstname,lastName=lastname,userEmail=email)
    return render_template("signup.html")

@app.route("/home",methods=['POST','GET'])
def home():
    return render_template("home.html")


if __name__== "__main__":
    app.run(debug=True)