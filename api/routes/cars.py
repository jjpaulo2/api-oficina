from typing import List, Union
from fastapi import APIRouter

from ..serializers import CarSerializer
from ..responses import JSONResponseMessage

from ..services.cars import CarsService


router = APIRouter(
    prefix='/cars',
    tags=['Carros']
)


@router.get('/', response_model=List[CarSerializer])
async def get_cars():
    '''
    Listar os carros cadastrados na oficina
    '''
    return await CarsService.get_all_cars()


@router.get('/{id}', response_model=CarSerializer)
async def get_one_car(id: int):
    '''
    Exibir os dados de apenas um carro por Id
    '''
    return await CarsService.get_one_car(id)


@router.post('/', response_model=JSONResponseMessage)
async def create_car(car: CarSerializer):
    '''
    Cadastrar novo carro
    '''
    return await CarsService.create_car(car)


@router.delete('/{id}', response_model=JSONResponseMessage)
async def remove_car(id: int):
    '''
    Exclui um carro por id
    '''
    return await CarsService.delete_car(id)
