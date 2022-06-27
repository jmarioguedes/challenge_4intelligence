__all__ = ['SupplierDomain']

from datetime import datetime
from typing import List

from models.supplier import EditSupplierModel
from models.supplier import InsertSupplierModel
from models.supplier import SupplierModel
from repository.supplier import SupplierRepository


class SupplierDomain:
    def __init__(self, repository: SupplierRepository):
        self._repository = repository

    async def prepare_repository(self):
        """Prepara o repositório.

        Verifica as condições de trabalho e providencia, entre outras coisas, a criação de índices.
        """
        await self._repository.prepare()

    async def create(self, supplier: InsertSupplierModel) -> SupplierModel:
        """Insere um novo fornecedor no banco de dados.

        Args:
            supplier: Instância de `InsertSupplierModel`

        Returns:
            Instancia de `SupplierModel`
        """
        new_supplier = SupplierModel(
            id=supplier.id_,
            name=supplier.name,
            company=supplier.company,
            created_at=datetime.utcnow(),
            amount_products=supplier.amount_products,
        )

        await self._repository.create(new_supplier.dict(by_alias=True))

        return new_supplier

    async def retrieve(self, supplier_id: str) -> SupplierModel:
        buffer = await self._repository.retrieve(supplier_id)
        return SupplierModel(**buffer)

    async def list(self) -> List[SupplierModel]:
        buffer = await self._repository.list()
        return [
            SupplierModel(**each)
            for each in buffer
        ]

    async def delete(self, supplier_id: str):
        await self._repository.delete(supplier_id)

    async def modify(self, supplier: EditSupplierModel) -> SupplierModel:
        await self._repository.modify(supplier.dict(by_alias=True, exclude_unset=True))
        buffer = await self.retrieve(supplier.id_)

        return buffer
