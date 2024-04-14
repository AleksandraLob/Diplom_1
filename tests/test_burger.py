from tests import data_burger
from mocks import BurgerMocks


class TestBurger:

    def test_add_ingredient_set_one_expected_one(self, burger):
        data_burger.set_ingredients(burger, 1)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_set_remove_one_expected_zero(self, burger):
        data_burger.set_ingredients(burger, 1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_set_buns_mock_bun_expected_bun(self, burger):
        bun = BurgerMocks.mock_bun()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_move_ingredient_add_ingrs_expected_change_posit(self, burger):
        add_ingr1 = data_burger.random_ingredient()
        burger.add_ingredient(add_ingr1)
        add_ingr2 = data_burger.random_ingredient()
        burger.add_ingredient(add_ingr2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [add_ingr2, add_ingr1]

    def test_get_price_burger_expected_price(self, burger):
        expected_price = data_burger.set_burger(burger)[4]
        assert burger.get_price() == expected_price

    def test_get_receipt_burger_expected_recept(self, burger):
        expected_receipt = data_burger.set_burger_and_get_receipt(burger)
        assert burger.get_receipt() == expected_receipt
