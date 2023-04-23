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
    "Calle 39 No 1540",
    "10 Downing Street",
    "Piazza del Colosseo, 1",
    "Rådhuspladsen 1",
    "Królewska 11A",
    "Rue de la Loi/Wetstraat 175",
    "Gran Via de les Corts Catalanes, 585",
    "Unter den Linden 77",
    "The Shard, 32 London Bridge Street",
    "Taipei 101, No. 7",
    "Salesforce Tower, 415 Mission Street",
    "7 Rue de Rivoli",
    "16 Via dei Condotti",
    "15 Kärntner Straße",
    "Max-Joseph-Platz 1",
    "Max-Joseph-Platz, No. 1",
    "Max-Joseph-Platz No 1",
    "1 Max-Joseph-Platz",
    "Max-Joseph-Platz, 1",
    "1, Max-Joseph-Platz",
    "Plaça de Catalunya 14",
    "Kärntner Straße 15",
    "Nieuwezijds Voorburgwal 165",
    "Avenue de Cortenbergh/Kortenberglaan 71-1"
]

parser = separator.Separator()

for address in addresses:
    print("\nAddress: ", address)
    print(parser.separate(address))
    print(parser.separate(address, parser="pandas"))
