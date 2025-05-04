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

@router.post(
    "/",
    response_model=ProductResponse,
    summary="Crear un nuevo producto",
    description="Crea un nuevo producto financiero con nombre, tasa de interés, montos y plazos válidos.",
    status_code=201,
    responses={422: {"description": "Errores de validación"}}
)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = CreateProductUseCase(repo)
    created = use_case.execute(**product.dict())
    return created


@router.get(
    "/",
    response_model=list[ProductResponse],
    summary="Listar todos los productos",
    description="Devuelve una lista de todos los productos registrados en el sistema."
)
def list_products(db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = ListProductsUseCase(repo)
    return use_case.execute()


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Obtener un producto por ID",
    description="Devuelve los detalles de un producto específico si existe.",
    responses={404: {"description": "Producto no encontrado"}}
)
def get_product(product_id: str, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = GetProductUseCase(repo)
    product = use_case.execute(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Actualizar un producto",
    description="Actualiza los datos de un producto existente por su ID.",
    responses={404: {"description": "Producto no encontrado"}}
)
def update_product(product_id: str, product_data: ProductUpdate, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = UpdateProductUseCase(repo)
    updated = use_case.execute(Product(id=product_id, **product_data.dict()))
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete(
    "/{product_id}",
    status_code=204,
    summary="Eliminar un producto",
    description="Elimina un producto por su ID si existe.",
    responses={404: {"description": "Producto no encontrado"}, 204: {"description": "Producto eliminado"}}
)
def delete_product(product_id: str, db: Session = Depends(get_db)):
    repo = SQLAlchemyProductRepository(db)
    use_case = DeleteProductUseCase(repo)
    product = repo.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    use_case.execute(product_id)
