from flask import Flask,flash,render_template,url_for,request,redirect
from flask_mysqldb import MySQL 
from werkzeug.security import generate_password_hash
import datetime
from config import config
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
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre,correo,clave,fechareg) VALUES (% ,% ,% ,%)",(nombre.upper, correo, clavecifrada, fechareg))
        db.connection.comint()
        return redirect(url_for('sUsuario'))

        return render_template(home.html)
    else:
        return render_template('signup.html')
@hope.router('/iUsuario')
    
@hope.route('/signin')
def signin():
    return render_template('/signin.html')




if __name__ == "__main__":
    hope.config.from_object(config['development'])
    hope.run(debug=True,port=3300) 

