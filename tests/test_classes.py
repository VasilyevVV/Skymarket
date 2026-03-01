import pytest

from src.Product import Product


def test_init_product(test_product_1, test_product_2):
    """Тест конструктора класса Product"""
    assert test_product_1.name == "Samsung Galaxy S23 Ultra"
    assert test_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert test_product_1.price == 108000.0
    assert test_product_1.quantity == 5

    assert test_product_2.name == "Xiaomi Redmi Note 14"
    assert test_product_2.description == "1024GB, Синий"
    assert test_product_2.price == 12000.0
    assert test_product_2.quantity == 14


def test_init_category(test_category_1, test_category_2):
    """Тест конструктора класса Category и подсчёта количества категорий и продуктов"""
    assert test_category_1.name == "Смартфоны"
    assert (
        test_category_1.description
        == "Смартфоны - средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(test_category_1.product_in_category) == 3

    # Проверка количества категорий у каждого экземпляра класса Category
    assert test_category_1.category_count == 2
    assert test_category_2.category_count == 2

    # Проверка количества товаров (экземпляров класса Product) в каждом экземпляре класса Category
    assert test_category_1.product_count == 3
    assert test_category_2.product_count == 3


def test_add_product(test_category_1, test_product_3):
    """Тест добавления продукта в список товаров категории"""
    x = test_category_1.product_count
    test_category_1.add_product(test_product_3)
    assert test_category_1.product_count == x + 1


def test_add_incorrect_product(test_category_1):
    """Тест добавления в категорию объекта, который не является классом Product"""
    with pytest.raises(ValueError) as exc_info:
        test_category_1.add_product(["some_product"])
    assert str(exc_info.value) == "Можно добавлять только объекты класса Product"


def test_new_product(test_new_product_dict):
    """Тест создания нового товара - объекта класса Product из словаря"""
    test_product = Product.new_product(test_new_product_dict)
    assert test_product.name == "Xiaomi Redmi Note 15"
    assert test_product.description == "128Gb, цвет: изумруд"
    assert test_product.price == 15000.0
    assert test_product.quantity == 2


# Тест при существующем товаре: выбирается максимальная цена, а количество складывается
def test_new_product_exist(test_new_product_dict2):
    """Тест создания нового объекта класса Product, если такой товар уже существует"""
    test_product = Product.new_product(test_new_product_dict2)
    assert test_product.name == "Xiaomi Redmi Note 15"
    assert test_product.description == "128Gb, цвет: изумруд"
    assert test_product.price == 15000.0
    assert test_product.quantity == 6


def test_products_property(test_category_1):
    """Тест приватного свойства '__products' в классе Category"""
    assert test_category_1.products == (
        "Samsung Galaxy S23 Ultra, 108000.0 руб. Остаток: 5 шт.\n"
        "Xiaomi Redmi Note 14, 12000.0 руб. Остаток: 14 шт.\n"
        "Infinix HOT 50, 11500.0 руб. Остаток: 10 шт.\n"
    )


def test_new_product_price(capsys, test_product_3):
    """Тест изменения цены на новую, больше текущей, и на ввод отрицательной цены"""
    test_product_3.price = -1000
    message1 = capsys.readouterr()
    assert message1.out.strip() == "Цена не должна быть нулевая или отрицательная"
    test_product_3.price = 18000.0
    assert test_product_3.price == 18000.0
