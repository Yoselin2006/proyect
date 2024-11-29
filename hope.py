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
@hope.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Crear el objeto Usuario con los datos del formulario
        Usuario = User(0, None, request.form['correo'], request.form['clave'], None, None)
        
        # Intentar autenticar al usuario
        UsuarioAutomatico = ModelUser.signin(db, Usuario)
        
        if UsuarioAutomatico is not None:
            # Verificar que la contraseña sea correcta
            if check_password_hash(UsuarioAutomatico.clave, request.form['clave']):
                # Loguear al usuario
                login_user(UsuarioAutomatico)
                
                # Guardar información en la sesión
                session["nombreU"] = UsuarioAutomatico.nombre
                session["perfilU"] = UsuarioAutomatico.perfil
                
                # Si el perfil es 'A', redirigir a admin, de lo contrario, a user
                if UsuarioAutomatico.perfil == 'A':
                    return redirect(url_for('admin'))
                else:
                    # Lógica para usuarios con perfil 'U' (usuario común)
                    selArt = db.connection.cursor()
                    selArt.execute("SELECT SUM(cantidad) AS TotalA FROM carrito WHERE idcliente = %s AND idventa IS NULL", [UsuarioAutomatico.id])
                    a = selArt.fetchone()
                    session['carrito'] = int(a[0] or 0)
                    selCarrito = db.connection.cursor()
                    selCarrito.execute("SELECT * FROM carrito")
                    p = selCarrito.fetchall()
                    return render_template('user.html', Productos=p, TotalA=a)
            else:
                flash('Contraseña incorrecta')
                return redirect(request.url)
        else:
            flash('Usuario no encontrado')
            return redirect(request.url)
    
    return render_template('signin.html')


@hope.route('/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return render_template('signin.html')

    if request.method == 'POST':
        # Obtener los valores del formulario
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        
        # Cifrar la contraseña
        clavecifrada = generate_password_hash(clave)
        
        # Obtener la fecha de registro
        fechareg = datetime.now()
        
        # Insertar el usuario en la base de datos
        UpUsuario = db.connection.cursor()
        UpUsuario.execute(
            "INSERT INTO usuario (nombre, correo, clave, fechareg, perfil) VALUES (%s, %s, %s, %s, %s)",
            (nombre.upper(), correo, clavecifrada, fechareg, 'U')
        )
        db.connection.commit()
        
        # Enviar un correo de bienvenida
        mensaje = Message(subject='Bienvenido a hope', recipients=[correo])
        mensaje.html = render_template('mail.html', nombre=nombre)
        mail.send(mensaje)
        
        return render_template('home.html')
    else:
        return render_template('signup.html')

@hope.route('/uUsuario/<int:id>', methods=['GET', 'POST'])
def uUsuario(id):
    if request.method == 'POST':
        # Obtener los valores del formulario
        nombre = request.form['nombre']
        correo = request.form['correo']
        perfil = request.form['perfil']
        
        # Actualizar usuario en la base de datos
        actuUsuario = db.connection.cursor()
        actuUsuario.execute(
            "UPDATE usuario SET nombre=%s, correo=%s, perfil=%s WHERE id=%s",
            (nombre, correo, perfil, id)
        )
        db.connection.commit()
        return redirect(url_for('admin'))  # Redirigir al admin después de la actualización

@hope.route('/sProducto', methods=['GET', 'POST'])
def sProducto():
    # Obtener productos desde la base de datos
    selProducto = db.connection.cursor()
    selProducto.execute("SELECT * FROM producto")
    p = selProducto.fetchall()
    selProducto.close()
    
    if session.get('perfilU') == 'A':
        return render_template('producto.html', productos=p)
    else:
        return render_template('user.html', productos=p)

if __name__ == "__main__":
      hope.run(debug=True,port=3300)

