from abc import ABCMeta
from abc import abstractmethod
from typing import Dict, List


class SupplierRepository(metaclass=ABCMeta):
    @abstractmethod
    async def prepare(self):
        raise NotImplementedError

    @abstractmethod
    async def create(self, supplier: Dict):
        raise NotImplementedError

    @abstractmethod
    async def retrieve(self, supplier_id: str):
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def modify(self, supplier: Dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, supplier_id: str):
        raise NotImplementedError
