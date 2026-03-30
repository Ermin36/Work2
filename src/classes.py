from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @property
    @abstractmethod
    def price(self) -> float: ...

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None: ...


class ProductLog:

    def __init__(self, *args, **kwargs):
        print(f'{self.__class__.__name__}{args}')


class Product(BaseProduct, ProductLog):
    name: str
    description: str
    _price: float
    quantity: int
    __products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        is_ok = False
        for item in Product.__products:
            if item.name == name:
                is_ok = True
                if price > item.price:
                    item.price = price
                    self._price = price
                self.quantity += item.quantity
                item.quantity = self.quantity

        if is_ok is False:
            Product.__products.append(self)

    def __str__(self) -> str:
        """Вывод строкового значения"""
        return f"{self.name}, {self._price} руб. Остаток {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """Сложение двух классов"""
        if self.__class__ is not other.__class__:
            raise TypeError('Типы продуктов должны быть одинаковыми')
        result = self._price * self.quantity + other._price * other.quantity
        return result

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создать новый продукт из данных словаря"""
        return cls(**product_data)

    @property
    def price(self) -> float:
        """Получить данные цены"""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Изменение цены.
        Если цена меньше или равна нулю, то не даст изменить.
        Если цена ниже текущей, то запросит подтверждение на изменение цены
        :param new_price: новая цена
        """
        if new_price > 0:
            if new_price < self._price:
                is_ok = False
                while not is_ok:
                    user_input = input("Уменьшить цену? y/n\n")
                    if user_input == "n":
                        is_ok = True
                    elif user_input == "y":
                        self._price = new_price
                        is_ok = True
                    else:
                        print("Не верное значение")
            else:
                self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Инициализация класса"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализация класса"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    name: str
    description: str
    _products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self._products = products
        self.__counter = 0
        self.__end = len(products)
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self) -> str:
        """Вывод строковых данных"""
        count = 0
        for product in self._products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count} шт."

    def __iter__(self) -> 'Category':
        """Итератор класса"""
        return self

    def __next__(self) -> Product:
        """Выдача следующего продукта"""
        if self.__counter < self.__end:
            self.__counter += 1
            return self._products[self.__counter-1]
        else:
            raise StopIteration

    def add_product(self, new_product: Product) -> None:
        """
        Добавление нового продукта в список
        :param new_product: новый продукт
        """
        if not isinstance(new_product, Product):
            raise TypeError('Не верный продукт')
        self._products.append(new_product)
        Category.product_count += 1
        self.__end = len(self._products)

    @property
    def products(self) -> str:
        """Получение списка продуктов"""
        result = ""

        for item in self._products:
            result += f"{item.name}, {item.price} руб. Остаток: {item.quantity} шт.\n"

        return result
