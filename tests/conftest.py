import pytest

from src.Category import Category
from src.Product import LawnGrass, Product, Smartphone


# Фикстура - тестовый продукт 1
@pytest.fixture
def test_product_1():
    return Product(name="Samsung Galaxy S23", description="256GB, Серый, 200MP камера", price=108000.0, quantity=5)


# Фикстура - тестовый продукт 2
@pytest.fixture
def test_product_2():
    return Product(name="Xiaomi Redmi Note 14", description="1024GB, Синий", price=12500.0, quantity=14)


# Фикстура - тестовый продукт 3
@pytest.fixture
def test_product_3():
    return Product(name="Infinix HOT 50", description="256GB, Серебристый", price=11500.0, quantity=10)


# Фикстура для тестирования класса Category
@pytest.fixture
def test_category_1(test_product_1, test_product_2, test_product_3):
    return Category(
        "Смартфоны",
        "Смартфоны - средство не только коммуникации, но и получения многих функций для удобства жизни",
        [test_product_1, test_product_2, test_product_3],
    )


# Фикстура для тестирования класса Category
@pytest.fixture
def test_category_2():
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром")


# Словарь для создания нового продукта
@pytest.fixture
def test_new_product_dict():
    return {"name": "Xiaomi Redmi Note 15", "description": "128Gb, цвет: изумруд", "price": 15000.0, "quantity": 2}


# Словарь для создания нового продукта с таким же именем
@pytest.fixture
def test_new_product_dict2():
    return {"name": "Xiaomi Redmi Note 15", "description": "128Gb, цвет: изумруд", "price": 10000.0, "quantity": 4}


# Фикстура для тестирования класса Smartphone
@pytest.fixture
def test_smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "512GB, Зелёный цвет, 500MP камера",
        108000.0,
        5,
        95.5,
        "S23 Ultra",
        512,
        "Изумрудный",
    )


# Фикстура для тестирования класса Smartphone
@pytest.fixture
def test_smartphone_2():
    return Smartphone("Xiaomi Redmi Note 15", "1024GB, Синий", 25000.0, 10, 90.3, "Note 15", 1024, "Синий")


# Фикстура для тестирования класса LawnGrass
@pytest.fixture
def test_lawgrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


# Фикстура для тестирования класса LawnGrass
@pytest.fixture
def test_lawgrass_2():
    return LawnGrass("Клевер газонный", "Цветочный газон", 200.0, 10, "Россия", "14 дней", "Белый, розовый")
