from unittest.mock import Mock

from tests import data


class BurgerMocks:

    @staticmethod
    def mock_bun():
        mock_bun = Mock()
        mock_bun.get_name.return_value = data.bun[0]
        mock_bun.get_price.return_value = data.bun[1]
        return mock_bun

    @staticmethod
    def mock_ingredient(type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        return mock_ingredient
