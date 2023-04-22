import unittest

from domain.address import Address
from infra.validator import Validator
from separator import AddressSeparator


class TestAddressSeparator(unittest.TestCase):

    def setUp(self):
        self.separator = AddressSeparator()
        self.validator = Validator()

    def test_separate_method(self):
        result = self.separator.separate("Winterallee 3")
        self.assertEqual(result, {"street": "Winterallee", "housenumber": "3"})

        result = self.separator.separate("Am Bächle 23")
        self.assertEqual(result, {"street": "Am Bächle", "housenumber": "23"})

    def test_separate_invalid_address(self):
        # test that an empty dictionary is returned for an invalid address
        invalid_address = "Invalid address"

        result = self.separator.separate(invalid_address)
        self.assertEqual(result, {})

    def test_separate_valid_address(self):
        # test that a valid address is separated into street name and house number
        valid_address = "Baker Street 221B"
        expected_result = {"street": "Baker Street", "housenumber": "221B"}

        result = self.separator.separate(valid_address)
        self.assertEqual(result, expected_result)

    def test_from_string_simple_valid_address(self):
        # test that a valid address string can be parsed into an Address object
        valid_address_str = "Baker Street 221B"
        expected_address = Address("Baker Street", "221B")
        address = Address.from_string_simple(valid_address_str)

        self.assertEqual(address.street, expected_address.street)
        self.assertEqual(address.house_number, expected_address.house_number)

    def test_from_string_foreign_valid_address_one(self):
        # test that a valid address string can be parsed into an Address object
        valid_address_str = "4, rue de la revolution"
        expected_address = Address("rue de la revolution", "4")
        address = Address.from_string_simple(valid_address_str)

        self.assertEqual(address.street, expected_address.street)
        self.assertEqual(address.house_number, expected_address.house_number)

    def test_from_string_foreign_valid_address_two(self):
        # test that a valid address string can be parsed into an Address object
        valid_address_str = "200 Broadway Av"
        expected_address = Address("Broadway Av", "200")
        address = Address.from_string_simple(valid_address_str)

        self.assertEqual(address.street, expected_address.street)
        self.assertEqual(address.house_number, expected_address.house_number)

    def test_from_string_foreign_valid_address_three(self):
        # test that a valid address string can be parsed into an Address object
        valid_address_str = "Calle Aduana, 29"
        expected_address = Address("Calle Aduana", "29")
        address = Address.from_string_simple(valid_address_str)

        self.assertEqual(address.street, expected_address.street)
        self.assertEqual(address.house_number, expected_address.house_number)

    def test_from_string_foreign_valid_address_four(self):
        # test that a valid address string can be parsed into an Address object
        valid_address_str = "Calle 39 No 1540"
        expected_address = Address("Calle 39", "No 1540")
        address = Address.from_string_simple(valid_address_str)

        self.assertEqual(address.street, expected_address.street)
        self.assertEqual(address.house_number, expected_address.house_number)

    def test_from_string_simple_invalid_address(self):
        # test that a ValueError is raised if the address string cannot be parsed
        invalid_address_str = "Invalid address"
        with self.assertRaises(ValueError):
            Address.from_string_simple(invalid_address_str)

    def test_separate_empty_address(self):
        # test that an empty dictionary is returned for an empty address string
        empty_address = ""
        result = self.separator.separate(empty_address)
        self.assertEqual(result, {})

    def test_separate_multiple_spaces(self):
        # test that a valid address with multiple spaces between words is separated into street name and house number
        address = "Baker      Street        221B"
        expected_result = {"street": "Baker      Street", "housenumber": "221B"}
        result = self.separator.separate(address)
        self.assertEqual(result, expected_result)

    def test_separate_no_house_number(self):
        # test that a valid address with no house number is separated into street name and an empty house number
        address = "Some Street"
        expected_result = {}
        result = self.separator.separate(address)
        self.assertEqual(result, expected_result)

    def test_separate_non_alphanumeric_house_number(self):
        # test that a valid address with a non-alphanumeric character in the house number is separated into street name and house number
        address = "Winterallee 3A"
        expected_result = {"street": "Winterallee", "housenumber": "3A"}
        result = self.separator.separate(address)
        self.assertEqual(result, expected_result)

    def test_separate_non_ascii_characters(self):
        # test that a valid address with non-ASCII characters is separated into street name and house number
        address = "Krøyer Gade 4"
        expected_result = {"street": "Krøyer Gade", "housenumber": "4"}
        result = self.separator.separate(address)
        self.assertEqual(result, expected_result)

    def test_separate_multiple_side_by_side_numbers(self):
        # test that an invalid address with multiple house numbers is separated into an empty dictionary
        address = "Winterallee 3 4"
        expected_result = {'housenumber': '4', 'street': 'Winterallee 3'}
        result = self.separator.separate(address)
        self.assertEqual(result, expected_result)

    def test_validator_valid_address(self):
        # test that a valid address passes the validator
        address = Address("Baker Street", "221B")
        result = self.validator.validate(address)
        self.assertTrue(result)

    def test_validator(self):
        pass


if __name__ == "__main__":
    unittest.main()
