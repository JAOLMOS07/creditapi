from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

HEX_COLOR_PATTERN = r"^#(?:[0-9a-fA-F]{6})$"

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    rate: float = Field(..., ge=0)
    min_amount: float = Field(..., gt=0)
    max_amount: float = Field(..., gt=0)
    min_term: int = Field(..., gt=0)
    max_term: int = Field(..., gt=0)
    color: str = Field(..., pattern=HEX_COLOR_PATTERN)

    @model_validator(mode="after")
    def validate_ranges(self) -> "ProductCreate":
        if self.min_amount > self.max_amount:
            raise ValueError("min_amount no puede ser mayor que max_amount")
        if self.min_term > self.max_term:
            raise ValueError("min_term no puede ser mayor que max_term")
        return self


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    rate: Optional[float] = Field(None, ge=0)
    min_amount: Optional[float] = Field(None, gt=0)
    max_amount: Optional[float] = Field(None, gt=0)
    min_term: Optional[int] = Field(None, gt=0)
    max_term: Optional[int] = Field(None, gt=0)
    color: Optional[str] = Field(None, pattern=HEX_COLOR_PATTERN)

    @model_validator(mode="after")
    def validate_ranges(self) -> "ProductUpdate":
        if self.min_amount > self.max_amount:
            raise ValueError("min_amount no puede ser mayor que max_amount")
        if self.min_term > self.max_term:
            raise ValueError("min_term no puede ser mayor que max_term")
        return self


class ProductResponse(ProductCreate):
    id: str
