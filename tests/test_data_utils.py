import unittest

from utils.data_utils import (
    dedupe_array,
    diff,
    pickle_it,
    sort_array,
    trim_array,
    unpickle_it,
)


class TestDataUtils(unittest.TestCase):
    def test_dedupe_array(self):
        my_duplicated_list = [
            ["dog", "beagle", "elsie"],
            ["cat", "tuxedo", "irma"],
            ["cat", "tabby", "irene"],
            ["dog", "beagle", "dorothy"],
            ["cat", "tabby", "irene"],
        ]
        deduped = dedupe_array(my_duplicated_list, 1)
        self.assertEqual(len(deduped), 3)

    def test_diff(self):
        pass

    def test_pickle_it(self):
        """docstring for test_pickle_it"""

    pass

    def test_sort_array(self):
        """docstring for test_sort_array"""

    pass

    def test_trim_array(self):
        my_list = [
            ["Vanilla", "Pistachio", "Strawberry", "Chocolate chip", "Neapolitan"],
            ["Strawberry", "Butter pecan", "Chocolate chip", "Vanilla", "Coffee"],
            ["Vanilla", "Neapolitan", "Strawberry", "Coffee", "Salted caramel"],
        ]
        trimmed = trim_array(my_list, [1, -1])
        self.assertEqual(len(trimmed[1]), 3)
        self.assertEqual(trimmed[0][-1], my_list[0][3])

    def test_unpickle_it(self):
        """docstring for test_unpickle_it"""

    pass
