from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from adapters.supplier_mongo import SupplierRepositoryMongo
from configuration import SETTINGS
from domains.supplier import SupplierDomain

_SUPPLIER_DOMAIN = None  # type: Optional[SupplierDomain]


async def get_supplier_domain() -> SupplierDomain:
    global _SUPPLIER_DOMAIN
    if not _SUPPLIER_DOMAIN:
        mongo_conn = AsyncIOMotorClient(SETTINGS.MONGO_URL)
        repository = SupplierRepositoryMongo(mongo_conn)
        _SUPPLIER_DOMAIN = SupplierDomain(repository)

    return _SUPPLIER_DOMAIN
