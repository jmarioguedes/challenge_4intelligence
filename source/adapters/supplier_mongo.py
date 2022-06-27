from typing import Dict, Final, List

from motor.motor_asyncio import AsyncIOMotorCollection
from motor.motor_asyncio import AsyncIOMotorDatabase

from repository.supplier import SupplierRepository

_COLLECTION_NAME = 'supplier'  # type: Final


class SupplierRepositoryMongo(SupplierRepository):
    def __init__(self, database: AsyncIOMotorDatabase):
        self._collection = database['supplier']  # type: AsyncIOMotorCollection

    async def prepare(self):
        await self._collection.create_index('id', name='id_unique', unique=True)

    async def create(self, supplier: Dict):
        await self._collection.insert_one(supplier)

    async def retrieve(self, supplier_id: str) -> Dict:
        buffer = await self._collection.find_one({'id': supplier_id})
        return buffer

    async def list(self) -> List[Dict]:
        buffer = []

        cursor = self._collection.find()
        cursor.sort('id', 1)
        async for each in cursor:
            buffer.append(each)

        return buffer

    async def modify(self, supplier: Dict):
        supplier_id = supplier.pop('id')

        await self._collection.update_one(
            {'id': supplier_id},
            {'$set': supplier}
        )

    async def delete(self, supplier_id: str):
        await self._collection.delete_one({'id': supplier_id})
