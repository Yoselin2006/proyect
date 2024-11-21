class Config:
    SECRET_KEY = 'NUNUNUNUNUNNUNUNUNUNUNUNUNUNUNUNUNUNU'
    BEDUG      = True


class DevelopmentConfig(Config):
        '''MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD= 'mysql'
        MYSQL_DB = 'hope' '''

        #pythonanywhere
        MYSQL_HOST = 'Yoselin2006.mysql.pythonanywhere-services.com'
        MYSQL_USER = 'Yoselin2006'
        MYSQL_PASSWORD= 'yose.123'
        MYSQL_DB = 'Yoselin2006$hope'

class MailConfig(Config):
    MAIL_SERVER         ='smtp.gmail.com'
    MAIL_PORT           = 587
    MAIL_USE_TLS        = True
    MAIL_USE_SSL        = False
    MAIL_USERNAME       = 'esmeralda.ortiz1779@alumnos.udg.mx'
    MAIL_PASSWORD       = 'fydj hvrj vcop vwnn'
    MAIL_ASCII_ATTACHMENTS = True
    MAIL_DEFAULT_SENDER = 
config = {
    'development': DevelopmentConfig,
    'mail'       : MailConfig
        }
        