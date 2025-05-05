import pytest
from domain.entities.product import Product
from application.use_cases.create_product import CreateProductUseCase
from fastapi import HTTPException
from unittest.mock import MagicMock


def test_create_product_success():
    repo = MagicMock()
    repo.find_by_name.return_value = None
    repo.create.side_effect = lambda product: product

    use_case = CreateProductUseCase(repo)
    result = use_case.execute(
        name="Producto X", rate=5.0, min_amount=1000, max_amount=5000,
        min_term=12, max_term=36, color="#FF0000"
    )

    assert result.name == "Producto X"
    assert result.color == "#FF0000"
    repo.create.assert_called_once()


def test_create_product_duplicate_name():
    repo = MagicMock()
    repo.find_by_name.return_value = Product(id="1", name="Producto X", rate=5.0, min_amount=1000, max_amount=5000,
                                             min_term=12, max_term=36, color="#FF0000")

    use_case = CreateProductUseCase(repo)

    with pytest.raises(HTTPException) as exc:
        use_case.execute(
            name="Producto X", rate=5.0, min_amount=1000, max_amount=5000,
            min_term=12, max_term=36, color="#FF0000"
        )
    assert exc.value.status_code == 422
