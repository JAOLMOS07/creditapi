from fastapi import HTTPException
from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product

class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: Product):
        existing = self.repository.get(product.id)
        if not existing:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return self.repository.update(product)
