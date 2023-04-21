import unittest

from address_separator import AddressSeparator


class TestAddressSeparator(unittest.TestCase):

    def setUp(self):
        self.address_separator = AddressSeparator()

    def test_separate_method(self):
        result = self.address_separator.separate("Winterallee 3")
        self.assertEqual(result, {"street": "Winterallee", "housenumber": "3"})

        result = self.address_separator.separate("Am Bächle 23")
        self.assertEqual(result, {"street": "Am Bächle", "housenumber": "23"})

        result = self.address_separator.separate("Invalid address")
        self.assertEqual(result, {})

    def test_validator(self):
        pass


if __name__ == "__main__":
    unittest.main()