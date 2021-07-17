from decouple import config

class AppSettings:
    HOST = config('APP_HOST', default='0.0.0.0', cast=str)
    PORT = config('APP_PORT', default=8080, cast=int)
    AUTO_RELOAD = config('APP_AUTO_RELOAD', default=False, cast=bool)
    DEBUG = config('APP_DEBUG', default=False, cast=bool)

class DatabaseSettings:
    DBMS = config('DB_MS', default='postgres', cast=str)
    HOST = config('DB_HOST', default='0.0.0.0', cast=str)
    PORT = config('DB_PORT', default=5432, cast=int)
    USERNAME = config('DB_USER', default='postgres', cast=str)
    PASSWORD = config('DB_PASS', default='12345', cast=str)
    DATABASE = config('DB_NAME', default='postgres', cast=str)
    
    URL = f'{DBMS}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    