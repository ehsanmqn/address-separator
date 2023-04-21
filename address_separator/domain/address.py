import re


class Address:
    """
    The Address class represents an address object with a street name and house number.
    """
    def __init__(self, street, house_number):
        self.street = street
        self.house_number = house_number

    @classmethod
    def from_string(cls, address_str):
        regex = r"^(?P<street>[\w\säöüÄÖÜß]+) (?P<house_number>[\d\s\w/]+)$"

        match = re.match(regex, address_str)

        if not match:
            raise ValueError(f"Invalid address: {address_str}")

        return cls(match.group("street"), match.group("house_number"))
