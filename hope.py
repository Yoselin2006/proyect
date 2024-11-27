from flask import Flask, render_template, url_for,redirect, request, flash,session
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL
from flask_mail import Mail,Message
from config import config
from models.entities.User import User
from models.ModelUser import ModelUser
from flask_login import LoginManager, login_user, logout_user, login_required
from datetime import datetime

hope = Flask(__name__)
#pythonanywhere
hope.config.from_object(config['development'])
hope.config.from_object(config['mail'])

db   = MySQL(hope)
mail = Mail(hope)
SigninManager = LoginManager(hope)

@SigninManager.user_loader
def load_user(id):
      return ModelUser.get_by_id(db,id)

@hope.route('/')
def home():
      return render_template('home.html')

@hope.route('/admin')
def admin():
      return render_template('admin.html')

@hope.route('/user')
def user():
      return redirect(url_for('sProducto'))

@hope.route('/signup',methods=['GET','POST'])
def signup():
      if request.method =='POST':
            nombre = request.form['nombre']
            correo = request.form['correo']
            clave  = request.form['clave']
            clavecifrada = generate_password_hash(clave)
            fechareg = datetime.datetime.now()
            UpUsuario = db.connection.cursor()
            UpUsuario.execute("INSERT INTO usuario (nombre,correo,clave,fechareg,perfil) VALUES (% ,% ,% ,% ,%)",(nombre.upper, correo, clavecifrada, fechareg, 'U'))
            db.connection.commit()
            mensaje = Message(subject = 'Bienvenido a hope',recitients = [correo]) 
            mensaje.html = render_template('mail.html', nombre = nombre)
            mail.send(mensaje)
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
            else:
      selArt = db.connection.cursor()
      selArt.execute("SELECT SUM(cantidad) AS TotalA FROM carrito WHERE idcliente = %s AND idventa IS NULL", ([usuarioAut.id],))
      a = selArt.fetchone()
      session['carrito'] = int (a[0] or 0)
      selCarrito = db.connection.cursor()
      selCarrito.execute("SELECT * FROM  carrito")
      p = selCarrito.fetchall()
      return render_template('user.html', Productos = p, TotalA = a )
      else:
      flash('Contraseña incorrecta')
      return redirect(request.url)
      else:
      flash('Usuario no encontrado')
      return redirect(request.url)
      return render_template('/signup.html')

@hope.router('/signoup, metods='['GET' , 'POST'])
def signin():
      logout_user()
      return render_template('signin.html')

@hope.router('/uUsuario', methods=('GET', 'POST'))
def uUsuario(id):
      nombre=request.form['nombre']
      correo=request.form['correo']
      perfil=request.form['perfil']
      actuUsuario = db.connection.cursor()
      actuUsuario.execute("UPDATE usuario SET nombre=%s, correo=%s, perfil=%s WERE id=%s",())

@hope.route('/sProducto', metods=['GET' , 'POST'])
def sProducto():
      selProducto = db.connection.cursor()
      selproducto = execute("SELECT = FROM producto")
      p = selproducto.fetchall
      selproducto.close()
      if session['perfilU'] == 'A'a
            return render_template('producto.html', productos=p)
      else:
            return render_template('user.html', productos=p)

if __name__ == "__main__":
      hope.run(debug=True,port=3300)

