from tortoise.contrib.pydantic import pydantic_model_creator

from .models.client import Client
from .models.client import Car
from .models.client import Service
from .models.client import ProvidedService

ClientSerializer = pydantic_model_creator(Client, name='Client')
CarSerializer = pydantic_model_creator(Car, name='Car')
ServiceSerializer = pydantic_model_creator(Service, name='Service')
ProvidedServiceSerializer = pydantic_model_creator(ProvidedService, name='ProvidedService')