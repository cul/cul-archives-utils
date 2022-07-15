import unittest

from cul_archives_utils.data_utils import dedupe_array, get_diff, sort_array, trim_array


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
        list1 = ["Vanilla", "Pistachio", "Strawberry", "Chocolate chip", "Neapolitan"]
        list2 = ["Strawberry", "Butter pecan", "Chocolate chip", "Vanilla", "Coffee"]
        diff = get_diff(list1, list2)
        self.assertEqual(diff, ['Pistachio', 'Neapolitan'])

    def test_sort_array(self):
        my_list = [
            ["Vanilla", "Pistachio", "Strawberry", "Chocolate chip", "Neapolitan"],
            ["Strawberry", "Butter pecan", "Chocolate chip", "Vanilla", "Coffee"],
            ["Vanilla", "Neapolitan", "Strawberry", "Coffee", "Salted caramel"],
        ]
        sorted_array = sort_array(my_list)
        self.assertEqual(sorted_array[0][0], "Strawberry")

    def test_trim_array(self):
        my_list = [
            ["Vanilla", "Pistachio", "Strawberry", "Chocolate chip", "Neapolitan"],
            ["Strawberry", "Butter pecan", "Chocolate chip", "Vanilla", "Coffee"],
            ["Vanilla", "Neapolitan", "Strawberry", "Coffee", "Salted caramel"],
        ]
        trimmed = trim_array(my_list, [1, -1])
        self.assertEqual(len(trimmed[1]), 3)
        self.assertEqual(trimmed[0][-1], my_list[0][3])
