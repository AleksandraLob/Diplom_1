from tests import data
from mocks import BurgerMocks
import random


def random_ingredient():
    rand_ingr = random.randint(1, 5)
    ingredient = BurgerMocks.mock_ingredient(data.ingredients[rand_ingr][0],
                                             data.ingredients[rand_ingr][1],
                                             data.ingredients[rand_ingr][2])
    return ingredient


def set_ingredients(burger, ingr_count):
    for ingredient in range(ingr_count):
        burger.add_ingredient(random_ingredient())
    return burger


def set_ingredient_get_data(burger):
    ingredient_data = []

    ingredient = random_ingredient()
    burger.add_ingredient(ingredient)

    ingredient_data.append(ingredient)
    ingredient_data.append(ingredient.get_type().lower())
    ingredient_data.append(ingredient.get_name())
    ingredient_data.append(ingredient.get_price())

    return ingredient_data


def set_bun_get_data(burger):
    bun_data = []

    bun = BurgerMocks.mock_bun()
    burger.set_buns(bun)

    bun_data.append(bun)
    bun_data.append(bun.get_price()*2)

    return bun_data


def set_burger(burger):
    burger_data = []
    ingrs_type = []
    ingrs_name = []
    ingrs_price = []

    for ingredient in range(4):
        ingredient = set_ingredient_get_data(burger)
        ingrs_type.append(ingredient[1])
        ingrs_name.append(ingredient[2])
        ingrs_price.append(ingredient[3])

    price = sum(ingrs_price) + set_bun_get_data(burger)[1]

    burger_data.append(burger)
    burger_data.append(set_bun_get_data(burger)[0])
    burger_data.append(ingrs_type)
    burger_data.append(ingrs_name)
    burger_data.append(price)

    return burger_data


def set_burger_and_get_receipt(burger):
    new_burger = set_burger(burger)

    receipt = \
        (f'(==== {new_burger[1].get_name()} ====)\n'
         f'= {new_burger[2][0]} {new_burger[3][0]} =\n'
         f'= {new_burger[2][1]} {new_burger[3][1]} =\n'
         f'= {new_burger[2][2]} {new_burger[3][2]} =\n'
         f'= {new_burger[2][3]} {new_burger[3][3]} =\n'
         f'(==== {new_burger[1].get_name()} ====)\n'
         f'\n'
         f'Price: {new_burger[4]}')

    return receipt
