from praktikum.database import Database


class TestDatabase:

    def test_count_available_buns(self):
        dbase = Database()

        assert len(dbase.available_buns()) == 3

    def test_count_available_ingredients(self):
        dbase = Database()

        assert len(dbase.available_ingredients()) == 6