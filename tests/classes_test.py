import pytest
from pytest_mock import MockerFixture

from src.classes import Category, Product


class TestClassCategory:

    @pytest.fixture
    def category(self) -> Category:
        """Инициализация тестового класса"""
        return Category(
            "TestCategory", "Testing", [Product("Test1", "test", 14.1, 2), Product("Test2", "desc", 23.1, 14)]
        )

    def test_init(self, category: Category) -> None:
        """Тест инициализации класса Category"""
        assert category.name == "TestCategory"
        assert category.description == "Testing"

    def test_counters(self) -> None:
        """Тест функций подсчёта категорий и продуктов"""
        Category("3", "", [])

        assert Category.category_count == 2
        assert Category.product_count == 0

    def test_add_product(self, category: Category) -> None:
        """Тест добавления нового продукта"""
        product = Product("Test", "testing", 14.2, 5)
        category.add_product(product)
        assert category.product_count == 3

    def test_get_products(self, category: Category) -> None:
        """Тест получения информации о продуктах"""
        result = category.products
        assert result == "Test1, 14.1 руб. Остаток: 6 шт.\nTest2, 23.1 руб. Остаток: 42 шт.\n"


class TestClassProduct:

    @pytest.fixture
    def product(self) -> Product:
        """Инициализация тестового класса"""
        return Product("Test", "Test product", 14.5, 1)

    def test_init(self, product: Product) -> None:
        """Тест инициализации класса Product"""
        assert product.name == "Test"
        assert product.description == "Test product"
        assert product.price == 14.5
        assert product.quantity == 6

    def test_get_info(self, product: Product) -> None:
        """Тест получения информации о продукте"""
        assert product.info == "Test, 14.5 руб. Остаток: 7 шт."

    def test_get_price(self, product: Product) -> None:
        """Тест получения цены"""
        assert product.price == 14.5

    def test_set_price(self, mocker: MockerFixture, product: Product) -> None:
        """Тест изменения цены"""
        product.price = 17.5
        assert product.price == 17.5

        mock_print1 = mocker.patch("builtins.print")
        product.price = 0
        assert product.price == 17.5
        mock_print1.assert_called_once()

        mock_input1 = mocker.patch("builtins.input", return_value="n")
        product.price = 15
        assert product.price == 17.5
        mock_input1.assert_called_once()

        mock_input2 = mocker.patch("builtins.input", return_value="y")
        product.price = 10
        assert product.price == 10
        mock_input2.assert_called_once()

        mocker.patch("builtins.input", side_effect=['t', 'n'])
        mock_print2 = mocker.patch("builtins.print")
        product.price = 3
        assert product.price == 10
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
        assert result.price == 180000.0
        assert result.quantity == 5
        assert result.description == "256GB, Серый цвет, 200MP камера"
