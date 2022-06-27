from typing import Dict

from motor.motor_asyncio import AsyncIOMotorClient

from repository.supplier import SupplierRepository


class SupplierRepositoryMongo(SupplierRepository):
    def __init__(self, mongo_conn: AsyncIOMotorClient):
        self._mongo_conn = mongo_conn

    async def insert(self, supplier: Dict):
        print('Olá Mundo!')

    async def update(self):
        pass

    async def modify(self):
        pass

    async def delete(self):
        pass

    async def retrieve(self):
        pass

    async def list(self):
        pass
