from typing import List, Union

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from tortoise.exceptions import DoesNotExist

from ..models.client import Client
from ..serializers import ClientSerializer
from ..responses import JSONResponseMessage

router = APIRouter(
    prefix='/clients',
    tags=['Clientes']
)


@router.get('/', response_model=List[ClientSerializer])
async def get_clients():
    '''
    Listar os clientes cadastrados na oficina
    '''
    queryset = await Client.all()
    return await ClientSerializer.from_queryset(queryset)


@router.get('/{id_or_cpf}', response_model=ClientSerializer)
async def get_one_client(id_or_cpf: Union[int, str]):
    '''
    Exibir os dados de apenas um cliente por id ou CPF
    '''
    try:
        if isinstance(id_or_cpf, int) and len(str(id_or_cpf)) == 11:
            query = {'cpf': id_or_cpf}
        elif isinstance(id_or_cpf, int):
            query = {'id': id_or_cpf}
        elif isinstance(id_or_cpf, str) and len(id_or_cpf) == 11:
            query = {'cpf': id_or_cpf}
        else:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='You did not pass a valid id or cpf'
            )

        client = await Client.get(**query)
        return await ClientSerializer.from_queryset_single(client)
    
    except DoesNotExist:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Client not found'
            )


@router.post('/', response_model=JSONResponseMessage)
async def create_client(client: ClientSerializer):
    '''
    Cadastrar novo cliente
    '''
    client_dict = client.dict(exclude_unset=True)
    client_object = await Client.create(**client_dict)
    return JSONResponseMessage(message='Client successfully created')


@router.delete('/{id_or_cpf}', response_model=JSONResponseMessage)
async def remove_client(id_or_cpf: Union[int, str]):
    '''
    Exclui um cliente por id ou CPF
    '''
    try:
        if isinstance(id_or_cpf, int) and len(str(id_or_cpf)) == 11:
            query = {'cpf': id_or_cpf}
        elif isinstance(id_or_cpf, int):
            query = {'id': id_or_cpf}
        elif isinstance(id_or_cpf, str) and len(id_or_cpf) == 11:
            query = {'cpf': id_or_cpf}
        else:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='You did not pass a valid id or cpf'
            )
            
        client_object = await Client.get(**query)
        await client_object.delete()
        return JSONResponseMessage(message='Client successfully deleted')

    except DoesNotExist:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Client not found'
            )
