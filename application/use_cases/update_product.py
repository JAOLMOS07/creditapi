from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product

class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: Product):
        return self.repository.update(product)
