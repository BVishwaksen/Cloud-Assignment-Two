from flask import Flask,render_template,request,session,logging,url_for,redirect,flash,g,send_from_directory,send_file
import sqlite3
import os


conn = sqlite3.connect('cloudassignment.db')
mycursor = conn.cursor()

username=''
password=''
firstname=''
lastname=''
email=''
fname=''
count=''

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=['GET','POST'])
def login():
    global username
    global password
    global firstname
    global lastname
    global email
    global fname
    global count

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
        firstname = myresult[0][1]
        lastname=myresult[0][2]
        email=myresult[0][3]
        fname=myresult[0][5]
        count=myresult[0][6]
        return render_template('home.html',firstName=firstname,lastName=lastname,userEmail=email,fname=fname,num_words=count)
    return render_template('login.html',error=error)

@app.route("/signup",methods=['POST','GET'])
def signup():
    global username
    global password
    global firstname
    global lastname
    global email
    global fname
    global count

    if request.method == 'POST':
        conn = sqlite3.connect('cloudassignment.db')
        mycursor = conn.cursor()
        username = request.form['userName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        email = request.form['userMail']
        password = request.form['password']
        fle = request.files['fname']
        fle.save(fle.filename)
        fname = fle.filename
        temp = open(fname,"r")
        content = temp.read()
        count = len(content.split())
        sql = "INSERT INTO users (username, firstname, lastname, email, userpassword,fname,count) VALUES (?, ?, ?, ?, ?,?,?)"
        val = (username,firstname,lastname,email,password,fle.filename,count)
        mycursor.execute(sql, val)
        conn.commit()
        return render_template('home.html',firstName=firstname,lastName=lastname,userEmail=email,fname=fname,num_words=count)
    return render_template("signup.html")

@app.route("/download",methods=['POST','GET'])
def home():
    global userName
    global password
    global firstname
    global lastname
    global email
    global fname
    global count
    
    print(os.path.join('\\',fname))
    return send_file(fname,as_attachment=True)
    print('called two')
    return render_template('home.html',firstName=firstname,lastName=lastname,userEmail=email,fname=fname,num_words=count)


if __name__== "__main__":
    app.run(debug=True)