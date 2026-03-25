import os

from src.utils import create_objects_from_json, read_json

# Путь к директории проекта с тестовым файлом JSON
TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def test_read_json():
    """Тест корректного чтения json-файла"""
    test_path = os.path.join(TEST_DIR, "test_products.json")
    result_dict = read_json(test_path)
    assert result_dict[0]["name"] == "Смартфоны"
    assert result_dict[1].get("name") == "Телевизоры"
    assert result_dict[2].get("description") == "Современные комфортные помощники на кухне"
    assert len(result_dict[0].get("products")) == 3
    assert len(result_dict[1].get("products")) == 1
    assert len(result_dict[2].get("products")) == 2


def test_read_json_error():
    """Тест чтения несуществующего файла"""
    assert read_json("file.txt") == {}


def test_create_objects_from_json():
    """Тест создания объектов - экземпляров классов Category и Product на основе чтения json-файла"""
    test_path = os.path.join(TEST_DIR, "test_products.json")
    result_dict = read_json(test_path)
    test_categories = create_objects_from_json(result_dict)
    assert str(test_categories[0]) == "Смартфоны, количество продуктов: 27 шт."
    assert str(test_categories[1]) == "Телевизоры, количество продуктов: 7 шт."
    assert str(test_categories[2]) == "Холодильники, количество продуктов: 11 шт."
    assert len(test_categories[0].product_in_category) == 3
    assert len(test_categories[1].product_in_category) == 1
    assert len(test_categories[2].product_in_category) == 2
