from typing import List, Union
from fastapi import APIRouter

from ..serializers import ClientSerializer
from ..responses import JSONResponseMessage

from ..services.clients import ClientsService


router = APIRouter(
    prefix='/clients',
    tags=['Clientes']
)


@router.get('/', response_model=List[ClientSerializer])
async def get_clients():
    '''
    Listar os clientes cadastrados na oficina
    '''
    return await ClientsService.get_all_clients()


@router.get('/{cpf}', response_model=ClientSerializer)
async def get_one_client(cpf: Union[int, str]):
    '''
    Exibir os dados de apenas um cliente por CPF
    '''
    return await ClientsService.get_one_client(id_or_cpf)


@router.post('/', response_model=JSONResponseMessage)
async def create_client(client: ClientSerializer):
    '''
    Cadastrar novo cliente
    '''
    return await ClientsService.create_client(client)


@router.delete('/{cpf}', response_model=JSONResponseMessage)
async def remove_client(cpf: Union[int, str]):
    '''
    Exclui um cliente por CPF
    '''
    return await ClientsService.delete_client(id_or_cpf)
