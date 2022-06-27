from mongomock_motor import AsyncMongoMockClient
import pytest

from adapters.supplier_mongo import SupplierRepositoryMongo
from domains.supplier import SupplierDomain


@pytest.fixture(scope='session')
def database():
    return AsyncMongoMockClient()['database']


@pytest.fixture
def supplier_domain(database):
    repository = SupplierRepositoryMongo(database)
    supplier_crud = SupplierDomain(repository)

    return supplier_crud

