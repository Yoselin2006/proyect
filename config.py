class Config:
    SECRET_KEY = 'NUNUNUNUNUNNUNUNUNUNUNUNUNUNUNUNUNUNU'
    DEDUG      = True


class DevelopmentConfig(Config):
        '''MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD= 'mysql'
        MYSQL_DB = 'hope' '''
class DevelopmentConfig(Config):
    # Configuración para PythonAnywhere
    MYSQL_HOST = 'Yoselin2006.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'Yoselin2006'
    MYSQL_PASSWORD = 'yose.123'
    MYSQL_DB = 'Yoselin2006$hope'  # Asegúrate de que esta sea la base de datos correcta

        
class MailConfig(Config):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'esmeralda.ortiz1779@alumnos.udg.mx'
    MAIL_PASSWORD = 'fydj hvrj vcop vwnn'  # ¡Asegúrate de que esta contraseña sea correcta!
    MAIL_ASCII_ATTACHMENTS = True
    MAIL_DEFAULT_SENDER = 'esmeralda.ortiz1779@alumnos.udg.mx'  # Aquí añades tu correo de envío
