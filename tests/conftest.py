import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def test_product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=108000.0, quantity=5
    )


@pytest.fixture
def test_product_2():
    return Product(name="Xiaomi Redmi Note 14", description="1024GB, Синий", price=12000.0, quantity=14)


@pytest.fixture
def test_product_3():
    return Product(name="Infinix HOT 50", description="256GB, Серебристый", price=11500.0, quantity=10)


@pytest.fixture
def test_category_1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни",
        [test_product_1, test_product_2, test_product_3],
    )


@pytest.fixture
def test_category_2():
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром")
