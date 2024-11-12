class config:
    SECRET_KEY = 'NUNUNUNUNUNNUNUNUNUNUNUNUNUNUNUNUNUNU'
    BEDUG      = True


class DevelopmentConfig(Config):
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD= 'mysql'
        MYSQL_DB = 'hope'

        pythonanywhere
         MYSQL_HOST = 'Yoselin2006.mysql.pythonanywhere-services.com'
        MYSQL_USER = 'Yoselin2006'
        MYSQL_PASSWORD= 'yose.123'
        MYSQL_DB = 'Yoselin2006$hope'

config = {
    'development': DevelopmentConfig
        }
        