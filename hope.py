from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL 
from werkzeug.security import generate_password_hash
from datetime import datetime
hope = Flask(__name__)
db   = MySQL(hope)

@hope.route('/')
def home(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        clavecifrada = generate_password_hash(clave)
        fechareg = datetime.now()

    return render_template('home.html')
@hope.route('/signup')
def signup(): 
    return render_template('signup.html')
@hope.route('/signin')
def signin(): 
    return render_template('signin.html')


if __name__ == "_main_":
    hope.run(debug=True,port=3300) 
