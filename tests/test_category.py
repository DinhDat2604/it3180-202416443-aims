import unittest
from aims.dvd import DigitalVideoDisc
from aims.category import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95),
        ]
        result = search_by_category(items, "Animation")
        self.assertEqual([d.title for d in result], ["The Lion King"])