from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from infrastructure.db import get_db
from infrastructure.db.repositories import SQLAlchemyProductRepository
from interfaces.api.schemas import ProductCreate, ProductResponse, ProductUpdate

from application.use_cases.create_product import CreateProductUseCase
from application.use_cases.get_product import GetProductUseCase
from application.use_cases.list_products import ListProductsUseCase
from application.use_cases.update_product import UpdateProductUseCase
from application.use_cases.delete_product import DeleteProductUseCase
from domain.entities.product import Product

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = CreateProductUseCase(repo)
    created = use_case.execute(**product.dict())
    return created

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = ListProductsUseCase(repo)
    return use_case.execute()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = GetProductUseCase(repo)
    product = use_case.execute(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: str, product_data: ProductUpdate, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = UpdateProductUseCase(repo)
    updated = use_case.execute(Product(id=product_id, **product_data.dict()))
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: str, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = DeleteProductUseCase(repo)
    use_case.execute(product_id)
