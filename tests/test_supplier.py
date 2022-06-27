import pytest

from mongomock_motor import AsyncMongoMockClient

from adapters.supplier_mongo import SupplierRepositoryMongo
from domains.supplier import SupplierDomain
from models.supplier import EditSupplierModel, InsertSupplierModel, SupplierModel


@pytest.fixture(scope='session')
def database():
    return AsyncMongoMockClient()['database']


@pytest.fixture
def supplier_domain(database):
    repository = SupplierRepositoryMongo(database)
    supplier_crud = SupplierDomain(repository)

    return supplier_crud


@pytest.mark.asyncio
async def test_collection_is_empty(database):
    count = await database['supplier'].count_documents({})
    assert count == 0


@pytest.mark.asyncio
async def test_crud_supplier_create(database, supplier_domain):
    supplier = InsertSupplierModel(
        id='BRCRD0028MG2ROML',
        name='João',
        company='4intellingence',
        amount_products=242
    )

    await supplier_domain.create(supplier)

    buffer = await database['supplier'].find({'id': 'BRCRD0028MG2ROML'}).to_list(lenght=1)

    assert buffer[0]['id'] == 'BRCRD0028MG2ROML'


@pytest.mark.asyncio
async def test_crud_supplier_item(database, supplier_domain):
    supplier = await supplier_domain.retrieve('BRCRD0028MG2ROML')

    assert isinstance(supplier, SupplierModel)


@pytest.mark.asyncio
async def test_crud_supplier_list(database, supplier_domain):
    suppliers = await supplier_domain.list()

    assert isinstance(suppliers, list)
    assert isinstance(suppliers[0], SupplierModel)
    assert suppliers[0].id_ == 'BRCRD0028MG2ROML'


@pytest.mark.asyncio
async def test_crud_supllier_modify(database, supplier_domain):
    supplier = EditSupplierModel(
        id='BRCRD0028MG2ROML',
        name='Maria',
    )
    buffer = await supplier_domain.modify(supplier)

    assert isinstance(buffer, SupplierModel)
    assert buffer.id_ == 'BRCRD0028MG2ROML'
    assert buffer.name == 'Maria'


@pytest.mark.asyncio
async def test_crud_supllier_delete(database, supplier_domain):
    await supplier_domain.delete('BRCRD0028MG2ROML')
    count = await database['supplier'].count_documents({})
    assert count == 0
