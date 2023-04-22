import re

# from pyspark.sql.functions import regexp_extract


class Address:
    """
    The Address class represents an address object with a street name and house number.
    """

    def __init__(self, street, house_number):
        self.street = street
        self.house_number = house_number

    @classmethod
    def from_string_simple(cls, address):
        # Regex patterns for street name and number
        patterns = [
            r'(?P<street>[\w\s]+) (?P<house_number>No \d+[a-zA-Z]*)',
            r'(?P<street>[\w\s]+) (?P<house_number>\d+[a-zA-Z]*\s?\w?)',
            r'(?P<house_number>\d+[a-zA-Z]*) (?P<street>[\w\s]+)',
            r'(?P<street>[\w\s]+),? (?P<house_number>\d+[a-zA-Z]*)',
            r'(?P<house_number>\d+[a-zA-Z]*)?,? (?P<street>[\w\s]+)'
        ]

        # Iterate over each patter to find a match
        for pattern in patterns:
            match = re.search(pattern, address)
            if match:
                groups = match.groupdict()

                if groups['street'] is not None and groups['house_number'] is not None:
                    street_name = groups['street'].strip()
                    house_number = groups['house_number'].strip()
                    return cls(street_name, house_number)

        raise ValueError(f"Invalid address: {address}")


