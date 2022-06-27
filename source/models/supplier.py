from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class InsertSupplierModel(BaseModel):
    id_: str = Field(alias='id', description='ID do fornecedor', min_length=16, max_length=16)
    name: str = Field(description='Nome do fornecedor')
    company: str = Field(description='Nome da empresa')
    amount_products: int = Field(description='Quantidade de produtos')

    class Config:
        schema_extra = {
            'example': {
                'id': 'BRCRD0028MG2ROML',
                'name': 'João',
                'company': '4intellingence',
                'amount_products': 242,
            }
        }


class EditSupplierModel(BaseModel):
    id_: str = Field(alias='id', description='ID do fornecedor', min_length=16, max_length=16)
    name: Optional[str] = Field(description='Nome do fornecedor')
    company: Optional[str] = Field(description='Nome da empresa')
    amount_products: Optional[int] = Field(description='Quantidade de produtos')

    class Config:
        schema_extra = {
            'example': {
                'id': 'BRCRD0028MG2ROML',
                'name': 'Maria',
            }
        }


class SupplierModel(BaseModel):
    id_: str = Field(alias='id', description='ID do fornecedor', min_length=16, max_length=16)
    name: str = Field(description='Nome do fornecedor')
    company: str = Field(description='Nome da empresa')
    created_at: datetime = Field(description='Data de registro')
    amount_products: int = Field(description='Quantidade de produtos')

    class Config:
        schema_extra = {
            'example': {
                'id': 'BRCRD0028MG2ROML',
                'name': 'João',
                'company': '4intellingence',
                'created_at': datetime(2022, 3, 2, 18, 13, 16),
                'amount_products': 242,
            }
        }
