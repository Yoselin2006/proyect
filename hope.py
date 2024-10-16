from flask import Flask,flash,render_template,url_for,request,redirect
from flask_mysqldb import MySQL 
from flask_login import LoginManager, login_user, logout_user
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
@hope.router('/uUsuario', methods=('GET', 'POST'))
def uUsuario(id):
        nombre=request.form['nombre']
        correo=request.form['correo']
        perfil=request.form['perfil']
        actuUsuario = db.connection.cursor()
        actuUsuario.execute("UPDATE usuario SET nombre=%s, correo=%s, perfil=%s WERE id=%s",())

def signup()
        if request.form == 'POST':
              Usuario = user (0, None,request.form['correo'],request.form['clave'],None, None)
              UsuarioAutomatico = ModelUser.signin(db,usuario)
        if UsuarioAutomatico is not None:
              if UsuarioAutomatico.clave:
                    login_user(UsuarioAutomatico)
                    if UsuarioAutomatico.pefil == 'A':
                           return render_template('admin.html')
                    else:
                           return render_template('user.html')
              else:
                    return 'contraseña incorrecta'
        else:
              return 'usuario inexsistente'
else:
        return render_template('/signup.html')
@hope.router('/signoup, metods='['GET' , 'POST'])
def signin():
      logout_user()
      return render_template('signin.html')




if __name__ == "__main__":
    hope.config.from_object(config['development'])
    hope.run(debug=True,port=3300) 

