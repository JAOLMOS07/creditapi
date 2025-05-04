from domain.repositories.product_repository import ProductRepository

class DeleteProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str):
        self.repository.delete(product_id)
