import sys
from os.path import dirname

# Add package path to syspath to prevent importing problems
sys.path.append(dirname(__file__))

from domain.address import Address
from infra.validator import Validator


class Separator:
    """
    The AddressSeparator class is responsible for separating the street name and house number from the address string.
    """

    def __init__(self):
        self.validator = Validator()

    def separate(self, address_str, parser="regex"):
        """
        Parse given address regarding the parser type specified by the user
        :param address_str: Input address string
        :param parser: Parser method
        :return: Dictionary object
        """

        # validate address_str before processing
        if not self.validator.validate(address_str):
            return {}

        # parse address into street and house number using Address class
        match parser:
            case "regex":
                address = Address.from_string_simple(address_str)
            case "pandas":
                address = Address.from_string_pandas(address_str)
            case _:
                raise ValueError("Parser method not supported.")

        # To improve the printing experience for non-unicode characters, dictionary used instead of `json
        return {"street": address.street, "housenumber": address.house_number}
