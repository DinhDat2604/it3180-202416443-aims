import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King", cost=1)]
        self.assertEqual(len(search_by_title(items, "lion")), 1)