from address_separator import address_separator

address = "Winterallee 3"

parser = address_separator.AddressSeparator()
result = parser.separate(address)

print(result)
