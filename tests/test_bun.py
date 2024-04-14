from praktikum.bun import Bun
from tests import data


class TestBun:

    def test_get_name_bun_name_expected_ok(self):
        bun = Bun(data.bun[0], None)
        assert bun.get_name() == data.bun[0]

    def test_get_price_bun_price_expected_ok(self):
        bun = Bun(None, data.bun[1])
        assert bun.get_price() == data.bun[1]
