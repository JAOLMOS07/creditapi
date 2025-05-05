from fastapi import HTTPException
from domain.repositories.product_repository import ProductRepository

class GetProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str):
        product = self.repository.get(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return product
