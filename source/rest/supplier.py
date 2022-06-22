from fastapi import APIRouter, Path

from models.supplier import SupplierModel, InsertSupplierModel, EditSupplierModel

router = APIRouter(prefix='/supplier')


@router.get('/{supplier_id}', response_model=SupplierModel)
async def retrieve_supplier(
        supplier_id: str = Path(description='ID do fornecedor')
) -> SupplierModel:
    pass


@router.post('/', response_model=SupplierModel)
async def post_supplier(
        supplier: InsertSupplierModel
) -> SupplierModel:
    pass


@router.put('/{supplier_id}', response_model=SupplierModel)
@router.patch('/{supplier_id}', response_model=SupplierModel)
async def edit_supplier(
        supplier: EditSupplierModel
) -> SupplierModel:
    pass


@router.delete('/{supplier_id}')
async def delete_supplier():
    pass
