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
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его подклассы"):
        test_category_1.add_product(["some_product"])


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
    assert message1.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    test_product_3.price = 18000.0
    assert test_product_3.price == 18000.0


def test_product_str(test_product_1, test_product_2, test_product_3):
    """Тест строкового представления для класса Product"""
    assert str(test_product_1) == "Samsung Galaxy S23 Ultra, 108000.0 руб. Остаток: 5 шт."
    assert str(test_product_2) == "Xiaomi Redmi Note 14, 12000.0 руб. Остаток: 14 шт."
    assert str(test_product_3) == "Infinix HOT 50, 11500.0 руб. Остаток: 10 шт."


def test_category_str(test_category_1):
    """Тест строкового представления для класса Category"""
    assert str(test_category_1) == "Смартфоны, количество продуктов: 29 шт."


def test_addition_products(test_product_1, test_product_2, test_product_3):
    """Тест магического метода __add__ для класса Product"""
    assert test_product_1 + test_product_2 == 708000.0
    assert test_product_1 + test_product_3 == 655000.0
    assert test_product_2 + test_product_3 == 283000.0


def test_add_product_error(test_product_2):
    """ "Тест ошибки при операции сложения для класса Product"""
    with pytest.raises(TypeError):
        result = test_product_2 + "NoProduct"


def test_smartphone_init(test_smartphone_2):
    """Тест конструктора класса Smartphone"""
    assert test_smartphone_2.name == "Xiaomi Redmi Note 15"
    assert test_smartphone_2.description == "1024GB, Синий"
    assert test_smartphone_2.price == 25000.0
    assert test_smartphone_2.quantity == 10
    assert test_smartphone_2.efficiency == 90.3
    assert test_smartphone_2.model == "Note 15"
    assert test_smartphone_2.memory == 1024
    assert test_smartphone_2.color == "Синий"


def test_lawgrass_init(test_lawgrass_2):
    """Тест конструктора класса LawnGrass"""
    assert test_lawgrass_2.name == "Клевер газонный"
    assert test_lawgrass_2.description == "Цветочный газон"
    assert test_lawgrass_2.price == 200.0
    assert test_lawgrass_2.quantity == 10
    assert test_lawgrass_2.country == "Россия"
    assert test_lawgrass_2.germination_period == "14 дней"
    assert test_lawgrass_2.color == "Белый, розовый"


def test_smartphone_add(test_smartphone_1, test_smartphone_2):
    """Тест операции сложения для класса Smartphone"""
    assert test_smartphone_1 + test_smartphone_2 == 790000.0


def test_smartphone_add_error(test_smartphone_1, test_lawgrass_1):
    """ "Тест ошибки при операции сложения для класса Smartphone"""
    with pytest.raises(TypeError, match="Операция может применяться только к смартфонам"):
        result = test_smartphone_1 + test_lawgrass_1


def test_lawgrass_add(test_lawgrass_1, test_lawgrass_2):
    """Тест операции сложения для класса LawnGrass"""
    assert test_lawgrass_1 + test_lawgrass_2 == 12000.0


def test_lawgrass_add_error(test_lawgrass_1, test_product_3):
    """ "Тест ошибки при операции сложения для класса LawnGrass"""
    with pytest.raises(TypeError, match="Операция может применяться только к товарам класса LawnGrass"):
        result = test_lawgrass_1 + test_product_3
