from typing import List, Union

from fastapi import status
from fastapi import HTTPException

from tortoise.exceptions import DoesNotExist
from tortoise.exceptions import IntegrityError

from ..models.client import Client
from ..serializers import ClientSerializer
from ..responses import JSONResponseMessage


class ClientsService:

    @staticmethod
    async def get_all_clients() -> List[ClientSerializer]:
        queryset = Client.all()
        return await ClientSerializer.from_queryset(queryset)


    @staticmethod
    async def get_one_client(cpf: Union[int, str]) -> ClientSerializer:
        try:
            client = await Client.get(cpf=cpf)
            return await ClientSerializer.from_queryset_single(client)
        
        except DoesNotExist:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Client not found'
                )


    @staticmethod
    async def create_client(client: ClientSerializer) -> JSONResponseMessage:
        try:
            client_dict = client.dict(exclude_unset=True)
            client_object = await Client.create(**client_dict)
            return JSONResponseMessage(message='Client successfully created')

        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Client with got CPF number already exists'
            )

    
    @staticmethod
    async def delete_client(cpf: Union[int, str]):
        try:
            client_object = await Client.get(cpf=cpf)
            await client_object.delete()
            return JSONResponseMessage(message='Client successfully deleted')

        except DoesNotExist:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Client not found'
                )
