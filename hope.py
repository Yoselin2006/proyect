from flask import Flask,flash,render_template,url_for,request,redirect, session
from flask_mysqldb import MySQL 
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
import datetime
from config import config

hope = Flask(__name__)
db   = MySQL(hope)
pythonanywhere
hope.config.from_object(config['development'])
hope.run(debug=True,port=3300)
@hope.route('/')
def home():
      return render_template('home.html')

@hope.route('/signup', methods =['GET','POST'])
def signup():
if request.method == 'POST':
      nombre = request.form['nombre']
      correo = request.form['correo']
      clave = request.form['clave']
      clavecifrada = generate_password_hash(clave)
      fechareg = datetime.datetime.now()
      regUsuario = db.connection.cursor()
      regUsuario.execute("INSERT INTO usuario (nombre,correo,clave,fechareg,perfil) VALUES (% ,% ,% ,% ,%)",(nombre.upper, correo, clavecifrada, fechareg, 'U'))
      db.connection.comint()
      return render_template('home.html')
else:
      return render_template('signup.html')

@hope.route('/signin', methods=['GET','POST'])
def signup():
      if request.form == 'POST':
      Usuario = User (0, None,request.form['correo'],request.form['clave'],None, None)
      UsuarioAutomatico = ModelUser.signin(db,usuario)
      if UsuarioAutomatico is not None:
      if UsuarioAutomatico.clave:
      login_user(UsuarioAutomatico)
      session["nombreU"]= UsuarioAutomatico.nombre
      session["perfilU"] = UsuarioAutomatico.perfil
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

@hope.router('/uUsuario', methods=('GET', 'POST'))
def uUsuario(id):
      nombre=request.form['nombre']
      correo=request.form['correo']
      perfil=request.form['perfil']
      actuUsuario = db.connection.cursor()
      actuUsuario.execute("UPDATE usuario SET nombre=%s, correo=%s, perfil=%s WERE id=%s",())

@hope.route('/sproducto', metods=['GET' , 'POST'])
def producto():
selproducto = db.connection.cursor()
selproducto = execute("SELECT = FROM producto")
prod = selproducto.fetchall
selproducto.close()
if session['perfilU'] == 'A'a
      return render_template('producto.html', producto.prod)
else:
      return render_template('user.html', producto.prod)

@hope.router('/signoup, metods='['GET' , 'POST'])
def signin():
      logout_user()
      return render_template('signin.html')


'''if __name__ == "__main__":
hope.config.from_object(config['development'])
hope.run(debug=True,port=3300)'''

