from typing import List, Optional

from fastapi import APIRouter, Depends, Path

from dependencies import get_supplier_domain
from domains.supplier import SupplierDomain
from models.supplier import SupplierModel, InsertSupplierModel, EditSupplierModel

router = APIRouter(prefix='/supplier')


@router.get('/{supplier_id}', response_model=SupplierModel)
async def retrieve_supplier(
        supplier_id: Optional[str] = Path(description='ID do fornecedor')
) -> SupplierModel:
    pass


@router.get('/', response_model=List[SupplierModel])
async def retrieve_supplier(
) -> SupplierModel:
    pass


@router.post('/', response_model=SupplierModel)
async def post_supplier(
        supplier: InsertSupplierModel,
        supplier_domain: SupplierDomain = Depends(get_supplier_domain),
) -> SupplierModel:
    buffer = await supplier_domain.insert(supplier)
    return buffer


@router.put('/{supplier_id}', response_model=SupplierModel)
@router.patch('/{supplier_id}', response_model=SupplierModel)
async def edit_supplier(
        supplier: EditSupplierModel
) -> SupplierModel:
    pass


@router.delete('/{supplier_id}')
async def delete_supplier():
    pass
