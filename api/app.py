from fastapi import FastAPI
from tortoise.contrib import fastapi

from .settings import AppSettings
from .settings import DatabaseSettings


app = FastAPI(debug=AppSettings.DEBUG)

fastapi.register_tortoise(
    app=app,
    db_url=DatabaseSettings.URL,
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)

