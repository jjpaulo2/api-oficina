from tortoise.models import Model
from tortoise import fields


class Permission(Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=20)
    name = fields.CharField(max_length=100)

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20)
    password = fields.CharField(max_length=100)
    name = fields.CharField(max_length=100)
    permissions = fields.ManyToManyField('models.Permission')
