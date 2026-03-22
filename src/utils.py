import json
import os

from src.Category import Category
from src.Product import Product


def read_json(path: str) -> dict:
    """Функция загружает данные из файла в формате JSON и преобразует их в словарь (dict)"""
    full_path = os.path.abspath(path)
    data_dict = {}
    try:
        with open(full_path, "r", encoding="UTF-8") as file:
            data_dict = json.load(file)
            return data_dict
    except FileNotFoundError:
        return data_dict


def create_objects_from_json(dict_data):
    """
    Функция принимает данные в виде словаря и создаёт объекты - экземпляры классов Category и Product
    на основе чтения данных из словаря.
    """
    if dict_data != {}:
        # пустой список для хранения объектов Category
        categories = []
        # запускаем цикл по категориям
        for category in dict_data:
            # пустой список для хранения объектов Product
            products = []
            # цикл по продуктам в категории
            for product in category["products"]:
                # Распаковка значений словаря - создание объекта Product и добавление его в список.
                products.append(Product(**product))
            # обновление списка продуктов для категории
            category["products"] = products
            # создание объекта Category и добавление его в список
            categories.append(Category(**category))
        return categories
