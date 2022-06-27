from typing import Optional

from mongomock_motor import AsyncMongoMockClient

from adapters.supplier_mongo import SupplierRepositoryMongo
from dependencies import get_supplier_domain
from domains.supplier import SupplierDomain
from service import app, app_api

from httpx import AsyncClient
import pytest

_MOCK_SUPPLIER_DOMAIN = None  # type: Optional[SupplierDomain]


def override_get_supplier_domain():
    global _MOCK_SUPPLIER_DOMAIN
    if not _MOCK_SUPPLIER_DOMAIN:
        database = AsyncMongoMockClient()['database']
        repository = SupplierRepositoryMongo(database)
        _MOCK_SUPPLIER_DOMAIN = SupplierDomain(repository)

    return _MOCK_SUPPLIER_DOMAIN


app_api.dependency_overrides[get_supplier_domain] = override_get_supplier_domain


@pytest.mark.asyncio
async def test_supplier_post():
    data = {
        'id': 'BRCRD0028MG2ROML',
        'name': 'João',
        'company': '4intellingence',
        'amount_products': 242,
    }

    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.post('/api/supplier/', json=data)

    assert response.status_code == 200
    assert response.json()['id'] == 'BRCRD0028MG2ROML'
    assert response.json()['name'] == 'João'


@pytest.mark.asyncio
async def test_supplier_get():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/api/supplier/BRCRD0028MG2ROML')

    assert response.status_code == 200
    assert response.json()['id'] == 'BRCRD0028MG2ROML'
    assert response.json()['name'] == 'João'


@pytest.mark.asyncio
async def test_supplier_list():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/api/supplier/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]['id'] == 'BRCRD0028MG2ROML'
    assert response.json()[0]['name'] == 'João'


@pytest.mark.asyncio
async def test_supplier_patch():
    data = {
        'id': 'BRCRD0028MG2ROML',
        'name': 'Maria',
    }
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.patch('/api/supplier/BRCRD0028MG2ROML', json=data)

    assert response.status_code == 200
    assert response.json()['id'] == 'BRCRD0028MG2ROML'
    assert response.json()['name'] == 'Maria'


@pytest.mark.asyncio
async def test_supplier_delete():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.delete('/api/supplier/BRCRD0028MG2ROML')

    assert response.status_code == 200

    count = await _MOCK_SUPPLIER_DOMAIN._repository._collection.count_documents({})
    assert count == 0
