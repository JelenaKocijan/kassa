import unittest
from kassa import menu_generator, get_item_id, price_calculation


class test_kassa(unittest.TestCase):

    def test_menu_generator(self):
        # arange

        stokroom_list = [{"id": 3, "naziv": "jabuka"}, {"id": 2, "naziv": "mandarina"}, {"id": 1, "naziv": "sljiva"}]
        # act
        rezultat = menu_generator(stokroom_list)

        # assert
        self.assertIn("1:sljiva", rezultat)
        self.assertIn("2:mandarina", rezultat)
        self.assertIn("3:jabuka", rezultat)
        self.assertTrue(isinstance(rezultat, str))

    def test_get_item_id(self):
        stokroom_list = [{"id": 3, "naziv": "jabuka"}, {"id": 2, "naziv": "mandarina"}, {"id": 1, "naziv": "sljiva"}]
        novi_rezultat = get_item_id(stokroom_list)
        self.assertIn(3, novi_rezultat)
        self.assertIn(1, novi_rezultat)
        self.assertIn(2, novi_rezultat)
        self.assertNotIn("sljiva", novi_rezultat)

        self.assertTrue(isinstance(novi_rezultat, list))

    def test_get_item_id_exception(self):
        koko = "koko-sanel"
        with self.assertRaises(Exception):
            get_item_id(koko)

    def test_price_calculation(self):
        dikt = {"id": 3, "naziv": "jabuka", "jedinicna_cena": "2450"}
        rezultat = price_calculation(3, dikt)
        self.assertEqual(7350, rezultat)
