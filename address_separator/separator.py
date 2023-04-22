from domain.address import Address
from infra.validator import Validator


class AddressSeparator:
    """
    The AddressSeparator class is responsible for separating the street name and house number from the address string.
    """

    def __init__(self):
        self.validator = Validator()

    def separate(self, address_str):
        # validate address_str before processing
        if not self.validator.validate(address_str):
            return {}

        # parse address into street and house number using Address class
        try:
            address = Address.from_string_simple(address_str)
            return {"street": address.street, "housenumber": address.house_number}
        except ValueError as error:
            return {}
