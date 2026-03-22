class Product:
    name: str
    description: str
    _price: float
    quantity: int
    __products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
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

    @property
    def info(self) -> str:
        """Получить информацию о продукте"""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."


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
        Category.category_count += 1
        Category.product_count = len(products)

    def add_product(self, new_product: Product) -> None:
        """
        Добавление нового продукта в список
        :param new_product: новый продукт
        """
        self._products.append(new_product)
        self.product_count = len(self._products)

    @property
    def products(self) -> str:
        """Получение списка продуктов"""
        result = ""

        for item in self._products:
            result += item.info + "\n"

        return result
