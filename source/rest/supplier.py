from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path

from dependencies import get_supplier_domain
from domains.supplier import SupplierDomain
from models.supplier import EditSupplierModel
from models.supplier import InsertSupplierModel
from models.supplier import SupplierModel

router = APIRouter(prefix='/supplier')


@router.get('/{supplier_id}', response_model=SupplierModel)
async def retrieve_supplier(
        supplier_id: str = Path(description='ID do fornecedor'),
        supplier_domain: SupplierDomain = Depends(get_supplier_domain),
) -> SupplierModel:
    supplier = await supplier_domain.retrieve(supplier_id)
    return supplier


@router.get('/', response_model=List[SupplierModel])
async def list_suppliers(
        supplier_domain: SupplierDomain = Depends(get_supplier_domain),
) -> List[SupplierModel]:
    suppliers = await supplier_domain.list()
    return suppliers


@router.post('/', response_model=SupplierModel)
async def post_supplier(
        supplier: InsertSupplierModel,
        supplier_domain: SupplierDomain = Depends(get_supplier_domain),
) -> SupplierModel:
    buffer = await supplier_domain.insert(supplier)
    return buffer


@router.patch('/{supplier_id}', response_model=SupplierModel)
async def edit_supplier(
        supplier: EditSupplierModel,
        supplier_domain: SupplierDomain = Depends(get_supplier_domain),
) -> SupplierModel:
    buffer = await supplier_domain.modify(supplier)
    return buffer


@router.delete('/{supplier_id}')
async def delete_supplier(
        supplier_id: str = Path(description='ID do fornecedor'),
        supplier_domain: SupplierDomain = Depends(get_supplier_domain),
):
    await supplier_domain.delete(supplier_id=supplier_id)
