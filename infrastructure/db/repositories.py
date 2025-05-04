from typing import Optional

from domain.repositories.product_repository import ProductRepository
from domain.entities.product import Product
from sqlalchemy.orm import Session

from infrastructure.db.models import ProductModel


class SQLAlchemyProductRepository(ProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product) -> Product:
        db_product = ProductModel(**product.__dict__)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)

        return self._to_domain(db_product)

    def get(self, product_id: str) -> Product:
        model = self.db.query(ProductModel).filter_by(id=product_id).first()
        return self._to_domain(model) if model else None

    def list(self) -> list[Product]:
        return [self._to_domain(p) for p in self.db.query(ProductModel).all()]

    def update(self, product: Product) -> Product:
        model = self.db.query(ProductModel).filter_by(id=product.id).first()
        if not model:
            return None
        for field, value in product.__dict__.items():
            setattr(model, field, value)
        self.db.commit()
        self.db.refresh(model)
        return self._to_domain(model)

    def delete(self, product_id: str) -> None:
        model = self.db.query(ProductModel).filter_by(id=product_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

    def _to_domain(self, model: ProductModel) -> Product:
        return Product(
            id=model.id,
            name=model.name,
            rate=model.rate,
            min_amount=model.min_amount,
            max_amount=model.max_amount,
            min_term=model.min_term,
            max_term=model.max_term,
            color=model.color,
        )

    def find_by_name(self, name: str) -> Optional[Product]:
        model = self.db.query(ProductModel).filter_by(name=name).first()
        return self._to_domain(model) if model else None
