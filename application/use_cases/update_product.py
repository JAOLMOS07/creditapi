from fastapi import HTTPException
from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product

class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: Product):
        existing = self.repository.find_by_name(product.name)
        if existing:
            if existing.id != product.id:
                raise HTTPException(status_code=422, detail="Ya existe un producto con ese nombre")
        return self.repository.update(product)
