
from pydantic import BaseModel,Field
from typing import Annotated



class ProductCreate(BaseModel):
    name: Annotated[str,Field(...,description="enter name of product")]
    price: Annotated[int,Field(...,description="enter price of product",gt=0)]



class ProductResponse(ProductCreate):
    id: int


class Config:
    from_attributes = True  # (Pydantic v2) replaces old 'orm_mode = True'
