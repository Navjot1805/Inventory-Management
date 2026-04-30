
from pydantic import BaseModel



class ProductCreate(BaseModel):
    name: str
    price: int



class ProductResponse(ProductCreate):
    id: int


class Config:
    from_attributes = True  # (Pydantic v2) replaces old 'orm_mode = True'
