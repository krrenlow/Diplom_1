from unittest.mock import Mock

from data import Data
from praktikum.bun import Bun


class TestBun:

    def test_success_create_bun(self):
        bun = Bun(Data.NAME_BUN, Data.PRICE_BUN)

        assert bun.name == Data.NAME_BUN and bun.price == Data.PRICE_BUN

    def test_get_bun_name(self):
        mock_bun_name = Mock()
        mock_bun_name.configure_mock(name='Булочка')

        assert Bun.get_name(mock_bun_name) == 'Булочка'

    def test_get_bun_price(self):
        mock_bun_price = Mock()
        mock_bun_price.configure_mock(price=123.50)

        assert Bun.get_price(mock_bun_price) == 123.50