import unittest

from ordereddict import OrderedDict

class OperationsTestCase(unittest.TestCase):
    def setUp(self):
        self.normal_dictionary = { "key": "value", "list": [1, 2, 3, "string"], "dict": {"null": None} }
        self.ordered_dictionary = OrderedDict(self.normal_dictionary)
         
    def tearDown(self):
        del self.normal_dictionary
        del self.ordered_dictionary

    def test_equal(self):
        self.assertEqual(
            self.ordered_dictionary,
            self.normal_dictionary,
        )
        
    def test_not_equal(self):
        self.assertNotEqual(
            self.ordered_dictionary,
            {},
        )
    
    def test_is_instance(self):
        self.assertIsInstance(self.ordered_dictionary, OrderedDict)
        
    # def test_is_instance(self):
    #     self.assertIsInstance(ordered_dictionary, dict)

if __name__ == '__main__':
    unittest.main(verbosity=2)