from tortoise.models import Model
from tortoise import fields


class Client(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    cpf = fields.CharField(max_length=11, unique=True)

    class PydanticMeta:
        exclude = ["id"]

class Car(Model):
    id = fields.IntField(pk=True)
    manufacturer = fields.CharField(max_length=20)
    model = fields.CharField(max_length=20)
    year = fields.IntField()
    client = fields.ManyToManyField('models.Client', on_delete=fields.CASCADE)

    class PydanticMeta:
        exclude = ["id"]

class Service(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    description = fields.TextField()
    price = fields.FloatField()

    class PydanticMeta:
        exclude = ["id"]

class ProvidedService(Model):
    id = fields.IntField(pk=True)
    start_date = fields.DateField()
    end_date = fields.DateField()
    car = fields.ForeignKeyField('models.Car')
    service = fields.ForeignKeyField('models.Service')
    price = fields.FloatField()

    class PydanticMeta:
        exclude = ["id"]
