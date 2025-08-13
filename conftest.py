from unittest.mock import Mock

import pytest


@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'Рисовая булка'
    bun.get_price.return_value = 150
    return bun


@pytest.fixture(scope='function')
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = 'Обычный'
    ingredient.get_price.return_value = 45
    ingredient.get_type.return_value = 'SAUCE'
    return ingredient


@pytest.fixture(scope='function')
def mock_ingredient_2():
    ingredient_2 = Mock()
    ingredient_2.get_name.return_value = 'Острый перец'
    ingredient_2.get_price.return_value = 100
    ingredient_2.get_type.return_value = 'FILLING'
    return ingredient_2