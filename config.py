class config:
    SECRET_KEY = 'NUNUNUNUNUNNUNUNUNUNUNUNUNUNUNUNUNUNUNUNUNnunununununununununununnuunuunununun'
    BEDUG      = True


    class DevelopmentConfig(Config):
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD= 'mysql'
        MYSQL_DB = 'hope'

        config = {
            'development' : DevelopmentConfig
        }
        