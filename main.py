from address_separator import separator

addresses = [
    "Winterallee 3",
    "Musterstrasse 45",
    "Blaufeldweg 123B",
    "Am Bächle 23",
    "Auf der Vogelwiese 23 b",
    "4, rue de la revolution",
    "200 Broadway Av",
    "Calle Aduana, 29",
    "Calle 39 No 1540"
]

parser = separator.Separator()

for address in addresses:
    print("Address: ", address)
    print(parser.separate(address))
    print(parser.separate(address, parser="pandas"))
