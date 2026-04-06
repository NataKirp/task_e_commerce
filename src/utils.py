import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """
    Функция для чтения данных их JSON-файла.
    :param path: Абсолютный путь к файлу.
    :return: Словарь с данными из файла.
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    print(type(data))
    return data


def create_objects_from_dict(data: dict) -> list[Category]:
    """
    Функция для создания объектов классов Category и Product из словаря.
    :param data: Словарь с данными.
    :return: Список объектов класса Category с вложенным списком объектов класса Product.
    """
    products_data = []
    for product_category_name in data:
        products = []
        for product in product_category_name["products"]:
            products.append(Product(**product))
        product_category_name["products"] = products
        products_data.append(Category(**product_category_name))
    return products_data


# if __name__ == "__main__":
#     json_data = read_json("../data/products.json")
#     out_data = create_objects_from_dict(json_data)
#
#     print(out_data[1].name)
#     print(out_data[1].products)
