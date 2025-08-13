import pytest

from data import Data
from praktikum import ingredient_types
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    @pytest.mark.parametrize(Data.param, Data.value)
    def test_get_price_burger(self, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price,
                              expected_burger_price):
        bun = Bun(bun_name, bun_price)
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_burger_price

    def test_get_receipt(self):
        bun = Bun(Data.NAME_BUN, Data.PRICE_BUN)
        ingredient_1 = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, Data.NAME_INGREDIENT_1,
                                  Data.PRICE_INGREDIENT_1)
        ingredient_2 = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, Data.NAME_INGREDIENT_2,
                                  Data.PRICE_INGREDIENT_2)
        ingredient_3 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, Data.NAME_INGREDIENT_3,
                                  Data.PRICE_INGREDIENT_3)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(1, 0)
        burger.remove_ingredient(0)

        assert burger.get_receipt() == Data.RECEIPT

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert (burger.bun.get_name() == 'Рисовая булка') and (burger.bun.get_price() == 150)

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_bun, mock_ingredient, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == mock_ingredient