import re

import pandas as pd


class Address:
    """
    The Address class represents an address object with a street name and house number.
    """

    # Regex patterns for street name and number
    patterns = [
        r'(?P<street>[\w\s]+) (?P<house_number>No \d+[a-zA-Z]*)',
        r'(?P<street>[\w\s]+) (?P<house_number>\d+[a-zA-Z]*\s?\w?)',
        r'(?P<house_number>\d+[a-zA-Z]*) (?P<street>[\w\s]+)',
        r'(?P<street>[\w\s]+),? (?P<house_number>\d+[a-zA-Z]*)',
        r'(?P<house_number>\d+[a-zA-Z]*)?,? (?P<street>[\w\s]+)'
    ]

    def __init__(self, street, house_number):
        self.street = street
        self.house_number = house_number

    @classmethod
    def from_string_simple(cls, address):
        """
        Parse string address using simple python regular expression
        :param address: Input address in string format
        :return: Address object
        """

        # Iterate over each patter to find a match
        for pattern in cls.patterns:
            match = re.search(pattern, address)

            if match:
                groups = match.groupdict()

                if groups['street'] is not None and groups['house_number'] is not None:
                    street_name = groups['street'].strip()
                    house_number = groups['house_number'].strip()
                    return cls(street_name, house_number)

        raise ValueError(f"Invalid address: {address}")

    @classmethod
    def from_string_pandas(cls, address):
        """
        Parse string address using pandas
        :param address: Input address in string format
        :return: Address object
        """

        # Create a DataFrame from the address string
        df = pd.DataFrame({'address': [address]})

        # Extract the street name and house number using the defined patterns
        for pattern in cls.patterns:
            result = df['address'].str.extract(pattern)

            # If both street name and house number are extracted, create an Address object
            if not result[['street', 'house_number']].isna().any().any():
                street_name = result['street'][0].strip()
                house_number = result['house_number'][0].strip()
                return cls(street_name, house_number)

        raise ValueError(f"Invalid address: {address}")
