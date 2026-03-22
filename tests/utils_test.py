from unittest.mock import MagicMock, mock_open

from pytest_mock import MockerFixture

from src.classes import Category, Product
from src.utils import read_json


class TestFunctionReadJson:

    def test_valid_read_json(self, mocker: MockerFixture) -> None:
        """Тест функции чтения json файла"""
        file_mock: MagicMock = mocker.patch("builtins.open", new_callable=mock_open, read_data="test")
        read_mock = mocker.patch("src.utils.json.load")
        read_mock.return_value = [
            {
                "name": "Смартфоны",
                "description": "Test",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
                ],
            }
        ]

        result: list[Category] = read_json("./testing/data.json")

        assert isinstance(result[0], Category)
        assert result[0].description == "Test"
        file_mock.assert_called_once()
        read_mock.assert_called_once()

    def test_invalid_read_json(self) -> None:
        """Тест ошибки при не верном пути к файлу"""

        result = read_json("./testing/data.json")

        assert result == []
