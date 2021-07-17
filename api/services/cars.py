from typing import List, Union

from fastapi import status
from fastapi import HTTPException

from tortoise.exceptions import DoesNotExist
from tortoise.exceptions import IntegrityError

from ..models.client import Car
from ..serializers import CarSerializer
from ..responses import JSONResponseMessage


class CarsService:

    @staticmethod
    async def get_all_cars() -> List[CarSerializer]:
        queryset = Car.all()
        return await CarSerializer.from_queryset(queryset)


    @staticmethod
    async def get_one_car(id: int) -> CarSerializer:
        try:
            car = await Car.get(id=id)
            return await CarSerializer.from_queryset_single(car)
        
        except DoesNotExist:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Car not found'
                )


    @staticmethod
    async def create_car(car: CarSerializer) -> JSONResponseMessage:
        try:
            car_dict = car.dict(exclude_unset=True)
            car_object = await Car.create(**car_dict)
            return JSONResponseMessage(message='Car successfully created')

        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Car with got data already exists'
            )

    
    @staticmethod
    async def delete_car(id: int):
        try:
            car_object = await Car.get(id=id)
            await car_object.delete()
            return JSONResponseMessage(message='Car successfully deleted')

        except DoesNotExist:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Car not found'
                )
