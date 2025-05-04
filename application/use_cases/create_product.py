from fastapi import HTTPException

from domain.entities.product import Product
from domain.repositories.product_repository import ProductRepository
from uuid import uuid4

class CreateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name: str, rate: float, min_amount: float, max_amount: float,
                min_term: int, max_term: int, color: str) -> Product:

        existing = self.repository.find_by_name(name)
        if existing:
            raise HTTPException(status_code=422, detail="Ya existe un producto con ese nombre")

        product = Product(
            id=str(uuid4()),
            name=name,
            rate=rate,
            min_amount=min_amount,
            max_amount=max_amount,
            min_term=min_term,
            max_term=max_term,
            color=color
        )
        return self.repository.create(product)
