# Проект 'Work 2'

## Установка

1. Клонировать репозиторий

    ``git clone https://github.com/Ermin36/MyProject.git``

2. Установка библиотек

    `poetry install` 
или `python -m poetry install`

3. Подключить в своём проекте модуль scr\processing

    ``from src.utils import read_json`` \- Импорт функции read_json

    `from src.classes import Category, Product` \- Импорт классов

## Использование

1. Функция ``read_json(path: str) -> list[Category]``

    Читает файл по пути `path`  возвращает список классов
    `Category`
    
    Использование:
    ```python
    from src.utils import read_json
    path = 'Ваш путь к файлу'
    data_list = read_json(path)
    ```

2. Класс `Category (name: str, description: str, list: list[Product])`
    
    Создание класса:
    ```python
    from src.classes import Category
    category = Category('Name', 'description', [])
    ```
   
3. Класс `Product (name: str, description: str, price: float, quantity: int)`

    Создание класса:
    ```python
    from src.classes import Product
    product = Product('Name', 'description', 13.1, 5)
   ```
    


