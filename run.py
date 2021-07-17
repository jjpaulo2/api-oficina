from uvicorn import run
from api.settings import AppSettings


configurations = {
    'app': 'api.app:app',
    'host': AppSettings.HOST,
    'port': AppSettings.PORT,
    'reload': AppSettings.AUTO_RELOAD,
    'debug': AppSettings.DEBUG 
}

def main(config: dict):
    run(**config)


if __name__ == '__main__':
    main(configurations)
    