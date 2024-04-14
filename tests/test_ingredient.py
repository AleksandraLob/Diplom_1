import pytest

from praktikum import ingredient_types
from praktikum.ingredient import Ingredient
from tests import data


class TestIngredient:

    @pytest.mark.parametrize('price', data.ingredients.keys())
    def test_get_price_ingr_price_expected_ok(self, price):
        ingredient_price = data.ingredients[price][2]
        ingredient = Ingredient(None, None, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize('name', data.ingredients.keys())
    def test_get_name_ingr_name_expected_ok(self, name):
        ingredient_name = data.ingredients[name][1]
        ingredient = Ingredient(None, ingredient_name, None)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_type', [ingredient_types.INGREDIENT_TYPE_SAUCE,
                                                 ingredient_types.INGREDIENT_TYPE_FILLING])
    def test_get_type_ingr_type_expected_ok(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, None, None)
        assert ingredient.get_type() == ingredient_type
