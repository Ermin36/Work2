import json

from src.classes import Category, Product


def read_json(path: str) -> list[Category]:
    """
    Функция читает данные json файла и возвращает список категорий
    :param path: путь к файлу
    :return: список категорий
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data_list: list[dict] = json.load(file)

            out_list = []
            for category in data_list:
                products = category.get("products", [])
                new_product_list = []
                for product in products:
                    new_product_list.append(Product(**product))

                category["products"] = new_product_list

                out_list.append(Category(**category))

            return out_list

    except FileNotFoundError as err:
        print(f"Файл не найден {path}\n {err}")
        return []
