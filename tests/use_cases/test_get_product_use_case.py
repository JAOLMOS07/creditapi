import pytest
from fastapi import HTTPException
from unittest.mock import MagicMock
from application.use_cases.get_product import GetProductUseCase
from domain.entities.product import Product

def test_get_product_success():
    mock_repo = MagicMock()
    mock_repo.get.return_value = Product(
        id="1", name="Producto A", rate=2.0, min_amount=100, max_amount=500,
        min_term=3, max_term=12, color="#0000FF"
    )
    use_case = GetProductUseCase(mock_repo)
    result = use_case.execute("1")

    assert result.id == "1"
    assert result.name == "Producto A"
    mock_repo.get.assert_called_once_with("1")

def test_get_product_not_found():
    mock_repo = MagicMock()
    mock_repo.get.return_value = None
    use_case = GetProductUseCase(mock_repo)

    with pytest.raises(HTTPException) as exc:
        use_case.execute("999")
    assert exc.value.status_code == 404
