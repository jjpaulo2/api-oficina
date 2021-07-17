from .settings import DatabaseSettings


TORTOISE_ORM = {
    'connections': {
        'default': DatabaseSettings.URL
    },
    'apps': {
        'models': {
            'models': [
                'api.models.client',
                'api.models.admin',
                'aerich.models'
            ],
            'default_connection': 'default',
        },
    },
}