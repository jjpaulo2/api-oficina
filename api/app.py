from fastapi import FastAPI
from tortoise.contrib import fastapi

from .settings import AppSettings
from .settings import DatabaseSettings

from .routes import clients
from .routes import cars

from .tags import TITLE
from .tags import DESCRIPTION
from .tags import TAGS_METADATAS


app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    openapi_tags=TAGS_METADATAS,
    debug=AppSettings.DEBUG,
)

fastapi.register_tortoise(
    app=app,
    db_url=DatabaseSettings.URL,
    modules={'models': [
        'api.models.client',
        'api.models.admin'
    ]},
    generate_schemas=False,
    add_exception_handlers=False
)

app.include_router(clients.router, prefix='/api')
app.include_router(cars.router, prefix='/api')
