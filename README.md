# Address Separator
Address Separator is a Python project that provides a simple way to parse and separate an addresses  with concatenated 
street names and numbers into its JSON format containing street address and the house number.

## Installation
### Manual
To install the Address Separator package, clone the repository from GitHub and install the requirements:
```bash
git clone https://github.com/your_username/address_separator.git
cd address_separator
pip install -r requirements.txt
```

### Pip
Use following commands to build and install the address separator package in your desired environment:
```bash
cd address_separator
bash install.sh
```

## Usage
The separator.py module located in the address_separator directory contains the main functionality of the package. 
To separate an address into its street and house number components, you can use following script:
```python
from address_separator import separator

parser = separator.Separator()

print(parser.separate("Calle Aduana, 29"))
```

You can also use the **main.py** containing example how to use the address_separator package.

## Project structure
The address-separator package implemented based on SOLID principles. The structure of the project is as follow:
```
address-separator/
    address_separator/
        domain/
            address.py
        infra/
            validator.py
        tests/
            test_address_separator.py
        separator.py
    install.sh
    requirements.txt
    setup.py
    main.py
    README.md
```

### separator.py
This file contains a class named **Separator**. This class has a method "separate" that receives an address string and an optional "parser" parameter.
The purpose of this class is to separate the street name and house number from the address string using either regex or pandas library, depending on the value of the "parser" parameter.

Before processing the address string, it performs validation using the "Validator" class defined in the "infra" module (The Validator class not implemented.)

Overall, this code implements a simple address parsing functionality that can be used for various applications, such as geocoding or database integration.

### address.py
The code contains a Python class named "Address". This class has two class methods - "from_string_simple" and "from_string_pandas" - that can be used to parse an address string and create an Address object.

The class defines a list of regex patterns that are used to match the street name and house number in the address string. The patterns cover various formats of addresses, such as "street number", "number street", "No number street", etc.

The "from_string_simple" method uses python's re module to iterate over the patterns and find a match for the given address string. If a match is found, it extracts the street name and house number from the match groups and creates an Address object with those values. If no match is found, it raises a ValueError indicating that the address is invalid.

The "from_string_pandas" method uses pandas library to extract the street name and house number from the address string. It creates a DataFrame with the address string and then iterates over the patterns to extract the street name and house number using the "str.extract()" method of pandas. If both street name and house number are extracted, it creates an Address object with those values. If no match is found, it raises a ValueError indicating that the address is invalid.

## Running tests
In order to run tests, run following command:

```bash
cd address_separator
python -m unittest
```

## Contributing
Contributions are always welcome! If you would like to contribute to the project, please follow these steps:

 - Fork the repository
 - Create your feature branch (git checkout -b feature/new-feature)
 - Commit your changes (git commit -m 'Add new feature')
 - Push to the branch (git push origin feature/new-feature)
 - Open a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
