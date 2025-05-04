# app/interfaces/api/schemas.py
from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    rate: float
    min_amount: float
    max_amount: float
    min_term: int
    max_term: int
    color: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    rate: Optional[float] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    min_term: Optional[int] = None
    max_term: Optional[int] = None
    color: Optional[str] = None


class ProductResponse(ProductCreate):
    id: str
