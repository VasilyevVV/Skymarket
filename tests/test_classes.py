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
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(test_category_1.products) == 3

    # Проверка количества категорий у каждого экземпляра класса Category
    assert test_category_1.category_count == 2
    assert test_category_2.category_count == 2

    # Проверка количества товаров (экземпляров класса Product) в каждом экземпляре класса Category
    assert test_category_1.product_count == 3
    assert test_category_2.product_count == 3
