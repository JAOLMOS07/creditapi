# app/domain/repositories/product_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.product import Product

class ProductRepository(ABC):

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get(self, product_id: str) -> Optional[Product]:
        pass

    @abstractmethod
    def list(self) -> List[Product]:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, product_id: str) -> None:
        pass
