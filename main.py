from address_separator import separator

parser = separator.AddressSeparator()

print(parser.separate("Winterallee 3"))
print(parser.separate("Musterstrasse 45"))
print(parser.separate("Blaufeldweg 123B"))
print(parser.separate("Am Bächle 23"))
print(parser.separate("Auf der Vogelwiese 23 b"))
print(parser.separate("4, rue de la revolution"))
print(parser.separate("200 Broadway Av"))
print(parser.separate("Calle Aduana, 29"))
print(parser.separate("Calle 39 No 1540"))
