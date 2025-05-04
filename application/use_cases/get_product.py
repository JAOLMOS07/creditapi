from domain.repositories.product_repository import ProductRepository

class GetProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str):
        return self.repository.get(product_id)
