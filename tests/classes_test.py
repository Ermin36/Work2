from src.classes import Category, Product
import pytest


class TestClassProduct:

    @pytest.fixture
    def product(self) -> Product:
        """Инициализация тестового класса"""
        return Product('Test', 'Test product', 14.5, 1)

    def test_init(self, product: Product) -> None:
        """Тест инициализации класса Product"""
        assert product.name == "Test"
        assert product.description == "Test product"
        assert product.price == 14.5
        assert product.quantity == 1

class TestClassCategory:

    @pytest.fixture
    def category(self) -> Category:
        """Инициализация тестового класса"""
        return Category('TestCategory', 'Testing', [
            Product('Test1', 'test', 14.1, 2),
            Product('Test2', 'desc', 23.1, 14)
        ])

    def test_init(self, category: Category) -> None:
        """Тест инициализации класса Category"""
        assert category.name == 'TestCategory'
        assert category.description == 'Testing'
        assert len(category.products) == 2

    def test_counters(self) -> None:
        """Тест функций подсчёта категорий и продуктов"""
        Category('2', '', [])

        assert Category.category_count == 2
        assert Category.product_count == 0