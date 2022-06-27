from abc import ABCMeta
from abc import abstractmethod
from typing import Dict


class SupplierRepository(metaclass=ABCMeta):
    @abstractmethod
    async def insert(self, supplier: Dict):
        raise NotImplementedError

    @abstractmethod
    async def update(self):
        raise NotImplementedError

    @abstractmethod
    async def modify(self):
        raise NotImplementedError

    @abstractmethod
    async def delete(self):
        raise NotImplementedError

    @abstractmethod
    async def retrieve(self):
        raise NotImplementedError

    @abstractmethod
    async def list(self):
        raise NotImplementedError
