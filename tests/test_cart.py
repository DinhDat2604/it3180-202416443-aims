import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"Disc {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("One too many")))
    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Disc", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_percent_out_of_range(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("B", cost=5.0))
        cart.add_dvd(DigitalVideoDisc("A", cost=9.0))
        self.assertEqual([d.cost for d in cart.sort_by_cost()], [5.0, 9.0])


if __name__ == "__main__":
    unittest.main()