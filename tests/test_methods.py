import unittest

from ordereddict import OrderedDict


class MethodsTestCase(unittest.TestCase):
    def setUp(self):
        self.normal_dictionary = { "key": "value", "list": [1, 2, 3, "string"], "dict": {"null": None} }
        self.ordered_dictionary = OrderedDict(self.normal_dictionary)
         
    def tearDown(self):
        del self.normal_dictionary
        del self.ordered_dictionary

    def test_keys(self):
        self.assertEqual(
            list(self.ordered_dictionary.keys()),
            list(self.normal_dictionary.keys()),
        )
        
    def test_values(self):
        self.assertEqual(
            list(self.ordered_dictionary.values()),
            list(self.normal_dictionary.values()),
        )
        
    def test_items(self):
        self.assertEqual(
            list(self.ordered_dictionary.items()),
            list(self.normal_dictionary.items()),
        )
        
    def test_copy(self):
        self.assertEqual(
            list(self.ordered_dictionary),
            list(self.ordered_dictionary.copy()),
        )
        
    def test_clear(self):
        self.assertGreater(
            len(self.normal_dictionary),
            0,
        )

        self.normal_dictionary.clear()
        
        self.assertEqual(
            len(self.normal_dictionary),
            0,
        )


if __name__ == '__main__':
    unittest.main()