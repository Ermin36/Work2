from itertools import product

import pytest
from pytest_mock import MockerFixture

from src.classes import Category, Product


class TestClassCategory:

    @pytest.fixture
    def category(self) -> Category:
        """Инициализация тестового класса"""
        return Category(
            "TestCategory", "Testing", [Product("test1", "test", 14.1, 2), Product("test2", "desc", 23.1, 14)]
        )

    def test_init(self, category: Category) -> None:
        """Тест инициализации класса Category"""
        assert category.name == "TestCategory"
        assert category.description == "Testing"
        assert len(category._products) == 2

    def test_str(self, category: Category) -> None:
        """Тест выдачи информации"""
        assert str(category) == 'TestCategory, количество продуктов: 32 шт.'

    def test_counters(self) -> None:
        """Тест функций подсчёта категорий и продуктов"""
        Category("3", "", [])

        assert Category.category_count == 3
        assert Category.product_count == 0

    def test_iter_next(self) -> None:
        """Тестирование системы итераций"""
        category_test = Category('Testing_Iter', 'test', [Product("test12", "test", 14.1, 2), Product("test21", "desc", 23.1, 14)])

        count = 0
        for item in category_test:
            count += 1
            assert isinstance(item, Product)
            assert isinstance(item.name, str)

        assert count == 2


    def test_add_product(self, category: Category) -> None:
        """Тест добавления нового продукта"""
        product1 = Product("Test", "testing", 14.2, 5)
        category.add_product(product1)
        assert category.product_count == 3

    def test_get_products(self, category: Category) -> None:
        """Тест получения информации о продуктах"""
        result = category.products
        assert result == "test1, 14.1 руб. Остаток: 8 шт.\ntest2, 23.1 руб. Остаток: 56 шт.\n"


class TestClassProduct:

    def test_init(self) -> None:
        """Тест инициализации класса Product"""
        product1 = Product("tester", "Test product", 14.5, 1)
        assert product1.name == "tester"
        assert product1.description == "Test product"
        assert product1._price == 14.5
        assert product1.quantity == 1

    def test_str(self) -> None:
        """Тест получения информации о продукте"""
        product1 = Product("Test3", "Test product", 14.5, 1)
        assert str(product1) == "Test3, 14.5 руб. Остаток 1 шт."

    def test_add(self) -> None:
        """Тест сложения дву классов"""
        product1 = Product("Test1", "test", 5.1, 10)
        product2 = Product('Test2', 'test', 7.2, 5)

        result = product1 + product2

        assert result == 87

    def test_get_price(self) -> None:
        """Тест получения цены"""
        product1 = Product("Test4", "Test product", 14.5, 1)
        assert product1.price == 14.5

    def test_set_price(self, mocker: MockerFixture) -> None:
        """Тест изменения цены"""
        product1 = Product("Test5", "Test product", 14.5, 1)
        product1.price = 17.5
        assert product1._price == 17.5

        mock_print1 = mocker.patch("builtins.print")
        product1.price = 0
        assert product1._price == 17.5
        mock_print1.assert_called_once()

        mock_input1 = mocker.patch("builtins.input", return_value="n")
        product1.price = 15
        assert product1._price == 17.5
        mock_input1.assert_called_once()

        mock_input2 = mocker.patch("builtins.input", return_value="y")
        product1.price = 10
        assert product1._price == 10
        mock_input2.assert_called_once()

        mocker.patch("builtins.input", side_effect=['t', 'n'])
        mock_print2 = mocker.patch("builtins.print")
        product1.price = 3
        assert product1._price == 10
        mock_print2.assert_called_once()

    def test_create_class_as_dict(self) -> None:
        """Тест создания класса из словаря"""
        data = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
        result = Product.new_product(data)

        assert result.name == "Samsung Galaxy S23 Ultra"
        assert result._price == 180000.0
        assert result.quantity == 5
        assert result.description == "256GB, Серый цвет, 200MP камера"
