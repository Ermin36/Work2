# Проект 'Work 2'
***
## Установка

1. Клонировать репозиторий

   `git clone https://github.com/Ermin36/MyProject.git`

2. Установка библиотек

    `poetry install` 
или `python -m poetry install`

3. Подключить в своём проекте модуль scr\processing

    `from src.utils import read_json` \- Импорт функции read_json

    `from src.classes import Category, Product` \- Импорт классов

---
## Использование

### Функции


1. [x] Функция ``read_json(path: str) -> list[Category]``

   Читает файл по пути `path`  возвращает список классов
    `Category`
    
    Использование:
    ```python
    from src.utils import read_json
    path = 'Ваш путь к файлу'
    data_list = read_json(path)
    ```

### Классы

   | Название            | Формат записи                                                                                                                |
   |---------------------|------------------------------------------------------------------------------------------------------------------------------|
   | Product             | Product(name: str, description: str, price: float, quantity: int                                                             |
   | Smartphone(Product) | Smartphone(name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str) |
   | LawnGrass(Product)  | LawnGrass(name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str)       |
   | Category            | Category(name: str, description: str, products: list[Product])                                                               |

### Обновление

Реализован абстракт-класс `BaseProduct` и лог-класс `ProductLog` для логирования создания новых
классов `Product`
