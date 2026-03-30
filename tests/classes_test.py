import pytest
from pytest_mock import MockerFixture
from unicodedata import category

from src.classes import Category, Product, LawnGrass, Smartphone

test_category = Category(
            "TestCategory", "Testing", [Product("test1", "test", 14.1, 2), Product("test2", "desc", 23.1, 14)]
        )

class TestClassCategory:

    @pytest.fixture
    def test_data(self) -> Category:
        """Инициализация тестового класса"""
        return test_category

    def test_init(self, test_data: Category) -> None:
        """Тест инициализации класса Category"""
        assert test_data.name == "TestCategory"
        assert test_data.description == "Testing"
        assert len(test_data) == 2

    def test_str(self, test_data: Category) -> None:
        """Тест выдачи информации"""
        assert str(test_data) == 'TestCategory, количество продуктов: 16 шт.'

    def test_counters(self) -> None:
        """Тест функций подсчёта категорий и продуктов"""
        Category("3", "", [])

        assert Category.category_count == 2
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

    def test_get_products(self, test_data: Category) -> None:
        """Тест получения информации о продуктах"""
        result = test_data.products
        assert result == "test1, 14.1 руб. Остаток: 2 шт.\ntest2, 23.1 руб. Остаток: 14 шт.\n"

    def test_valid_add_product(self, test_data: Category) -> None:
        """Тест добавления нового продукта"""
        product1 = Product("Test", "testing", 14.2, 5)
        test_data.add_product(product1)
        assert test_data.product_count == 3

    # noinspection PyTypeChecker
    def test_invalid_add_product(self, test_data: Category) -> None:
        """Тест функции на ошибку"""
        with pytest.raises(TypeError) as err:
            test_data.add_product('test')

        assert str(err.value) == "Не верный продукт"

    def test_middle_price(self) -> None:
        """Тест функции получения средней стоимости продуктов и ошибки"""
        test_data = Category('Test', 'testing', [])

        assert test_data.middle_price() == 0.0

        test_data.add_product(Product('test1', 'test', 20.0, 1))
        test_data.add_product(Product('test2', 'test', 40.0, 2))

        result = test_data.middle_price()

        assert result == 30.0


class TestClassProduct:

    def test_init_valid(self) -> None:
        """Тест инициализации класса Product"""
        product1 = Product("tester", "Test product", 14.5, 1)
        assert product1.name == "tester"
        assert product1.description == "Test product"
        assert product1._price == 14.5
        assert product1.quantity == 1

    def test_init_invalid(self) -> None:
        """Тест ошибки"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
             Product("tester", "Test product", 14.5, 0)

    def test_log(self, mocker: MockerFixture) -> None:
        """Тест класса ProductLog"""
        print_mock = mocker.patch('builtins.print')

        Product('Test', '5', 12.0, 4)

        print_mock.assert_called_once_with("Product('Test', '5', 12.0, 4)")

    def test_str(self) -> None:
        """Тест получения информации о продукте"""
        product1 = Product("Test3", "Test product", 14.5, 1)
        assert str(product1) == "Test3, 14.5 руб. Остаток 1 шт."

    def test_valid_add(self) -> None:
        """Тест сложения двух классов"""
        product1 = Product("Test1", "test", 5.1, 10)
        product2 = Product('Test2', 'test', 7.2, 5)

        result = product1 + product2

        assert result == 87

    def test_invalid_add(self) -> None:
        """Тест функции на корректность ошибки"""
        product1 = Product("Test1", "test", 5.1, 10)
        product2 = Smartphone("Test11", 'test', 12.1, 5, 32.1, '1', 1, '1')

        with pytest.raises(TypeError) as err:
            product1 + product2

        assert str(err.value) == "Типы продуктов должны быть одинаковыми"

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


class TestClassSmartphone:

    def test_init(self) -> None:

        result = Smartphone('Test', 'testing', 5.1, 1, 91.2, 'model', 12, 'color')

        assert result.name == "Test"
        assert result.efficiency == 91.2
        assert result.model == 'model'
        assert result.memory == 12
        assert result.color == 'color'


class TestClassLawnGrows:

    def test_init(self) -> None:

        result = LawnGrass('Test', 'testing', 12.1, 1, "cont", 'ger', 'color')

        assert result.name == "Test"
        assert result.country == 'cont'
        assert result.germination_period == 'ger'
        assert result.color == 'color'