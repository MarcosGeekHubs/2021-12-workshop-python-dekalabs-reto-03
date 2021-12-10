from unittest import TestCase

from src.main import get_frequent_words
from tests.helpers import EXPECTED_FREQUENT_WORDS


class BookTestCase(TestCase):
    def test_frequent_words(self):
        amount = len(EXPECTED_FREQUENT_WORDS)
        frequent_words = get_frequent_words(amount=amount)
        self.assertEqual(frequent_words, EXPECTED_FREQUENT_WORDS)

    def test_top_three_frequent_words(self):
        frequent_words = get_frequent_words(amount=3)
        self.assertEqual(frequent_words, EXPECTED_FREQUENT_WORDS[:3])
