import pytest
from interfaces.api.schemas import ProductCreate
from pydantic import ValidationError

def test_valid_product_create():
    product = ProductCreate(
        name="A",
        rate=1.5,
        min_amount=100,
        max_amount=200,
        min_term=6,
        max_term=12,
        color="#123ABC"
    )
    assert product.name == "A"

def test_invalid_color_format():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="A",
            rate=1.5,
            min_amount=100,
            max_amount=200,
            min_term=6,
            max_term=12,
            color="red"
        )

def test_invalid_amount_range():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="A",
            rate=1.5,
            min_amount=300,
            max_amount=200,
            min_term=6,
            max_term=12,
            color="#123ABC"
        )
