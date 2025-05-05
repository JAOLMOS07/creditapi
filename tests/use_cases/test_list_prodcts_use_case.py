from unittest.mock import MagicMock
from domain.entities.product import Product
from application.use_cases.list_products import ListProductsUseCase

def test_list_products():
    mock_repo = MagicMock()
    mock_repo.list.return_value = [
        Product(id="1", name="A", rate=1.0, min_amount=100, max_amount=500, min_term=3, max_term=12, color="#111111"),
        Product(id="2", name="B", rate=2.0, min_amount=200, max_amount=600, min_term=6, max_term=18, color="#222222"),
    ]
    use_case = ListProductsUseCase(mock_repo)
    result = use_case.execute()

    assert len(result) == 2
    assert result[0].name == "A"
    assert result[1].name == "B"
