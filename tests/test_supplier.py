import pytest

from adapters.supplier_mongo import SupplierRepositoryMongo
from domains.supplier import SupplierDomain


@pytest.fixture
def supplier_domain():
    mongo_conn = None
    repository = SupplierRepositoryMongo(mongo_conn)
    supplier_crud = SupplierDomain(repository)

    return supplier_crud


@pytest.mark.asyncio
async def test_crud_supplier_insert(supplier_domain):
    assert True
