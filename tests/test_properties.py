import unittest

from ordereddict import OrderedDict

class PropertiesTestCase(unittest.TestCase):
    def setUp(self):
        self.normal_dictionary = { "key": "value", "list": [1, 2, 3, "string"], "dict": {"null": None} }
        self.ordered_dictionary = OrderedDict(self.normal_dictionary)
         
    def tearDown(self):
        del self.normal_dictionary
        del self.ordered_dictionary

    def test_length(self):
        self.assertEqual(
            len(self.ordered_dictionary),
            len(self.normal_dictionary),
            "Should be same length"
        )
		

    def test_str(self):
        self.assertEqual(
            str(self.ordered_dictionary), 
            "OrderedDict({'key': 'value', 'list': [1, 2, 3, 'string'], 'dict': {'null': None}})",
        )


    def test_repr(self):
        self.assertEqual(
            repr(self.ordered_dictionary), 
            "OrderedDict({'key': 'value', 'list': [1, 2, 3, 'string'], 'dict': {'null': None}})",
        )

    def test_noop(self):
        pass


if __name__ == '__main__':
    unittest.main()