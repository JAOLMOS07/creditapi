import pytest
from fastapi import HTTPException
from unittest.mock import MagicMock
from domain.entities.product import Product
from application.use_cases.update_product import UpdateProductUseCase

def test_update_product_success():
    mock_repo = MagicMock()
    existing_product = Product(
        id="1", name="Producto A", rate=2.0, min_amount=100, max_amount=500,
        min_term=3, max_term=12, color="#0000FF"
    )
    mock_repo.get.return_value = existing_product
    mock_repo.update.side_effect = lambda product: product

    use_case = UpdateProductUseCase(mock_repo)
    result = use_case.execute(existing_product)

    assert result.id == "1"
    mock_repo.update.assert_called_once_with(existing_product)

def test_update_product_not_found():
    mock_repo = MagicMock()
    mock_repo.get.return_value = None
    use_case = UpdateProductUseCase(mock_repo)

    with pytest.raises(HTTPException) as exc:
        use_case.execute(Product(
            id="1", name="Producto A", rate=2.0, min_amount=100, max_amount=500,
            min_term=3, max_term=12, color="#0000FF"
        ))
    assert exc.value.status_code == 404
