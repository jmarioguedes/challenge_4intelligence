from typing import Final, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from adapters.supplier_mongo import SupplierRepositoryMongo
from configuration import SETTINGS
from domains.supplier import SupplierDomain

_DATABASE_NAME = '4intelligence'  # type: Final
_SUPPLIER_DOMAIN = None  # type: Optional[SupplierDomain]


async def get_supplier_domain() -> SupplierDomain:
    global _SUPPLIER_DOMAIN
    if not _SUPPLIER_DOMAIN:
        database = AsyncIOMotorClient(SETTINGS.MONGO_URL)[_DATABASE_NAME]
        repository = SupplierRepositoryMongo(database)
        _SUPPLIER_DOMAIN = SupplierDomain(repository)

    return _SUPPLIER_DOMAIN


async def startup():
    supplier_domain = await get_supplier_domain()
    await supplier_domain.prepare_repository()
