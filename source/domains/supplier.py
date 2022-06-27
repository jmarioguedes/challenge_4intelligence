__all__ = ['SupplierDomain']

from models.supplier import InsertSupplierModel
from repository.supplier import SupplierRepository


class SupplierDomain:
    def __init__(self, repository: SupplierRepository):
        self._repository = repository

    async def insert(self, supplier: InsertSupplierModel):
        await self._repository.insert(supplier.dict())

    async def retrieve(self):
        pass

    async def list(self):
        pass

    async def delete(self):
        pass

    async def modify(self):
        pass
