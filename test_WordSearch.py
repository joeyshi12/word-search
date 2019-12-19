import unittest

from WordSearch import *


class TestWordSearch(unittest.TestCase):

    def test_is_valid_word(self):
        self.assertTrue(is_valid_word('word'))

    def test_is_invalid_word(self):
        self.assertFalse(is_valid_word('wordnt'))

    def test_next_words_empty_chars(self):
        word = 'wor'
        chars = []
        self.assertEqual(next_words(word, chars), [])

    def test_next_words_nonempty_chars(self):
        word = 'wor'
        chars = ['p', 'b', 'd']
        self.assertEqual(next_words(word, chars), ['worp', 'worb', 'word'])

    def test_search_words_empty_chars_zero_n(self):
        chars = []
        n = 0
        self.assertEqual(search_words(chars, n), [])

    def test_search_words_empty_chars_nonzero_n(self):
        chars = []
        n = 2
        self.assertEqual(search_words(chars, n), [])

    def test_search_words_nonempty_chars_zero_n(self):
        chars = ['a']
        n = 0
        self.assertEqual(search_words(chars, n), [])

    def test_search_words_nonempty_chars_nonzero_n(self):
        chars = ['s', 'a', 'n', 'd']
        n = 3
        self.assertEqual(search_words(chars, n), ['sad', 'and', 'ads'])
