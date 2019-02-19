from libs.parser import AddressParser


def test_valid_parsing():
    addresses = [
        ('Winterallee 3', {'street': 'Winterallee', 'housenumber': '3'}),
        ('Musterstrasse 4', {'street': 'Musterstrasse', 'housenumber': '4'}),
        ('Blaufeldweg 123b', {'street': 'Blaufeldweg', 'housenumber': '123b'}),
        ('Am Bächle 23', {'street': 'Am Bächle', 'housenumber': '23'}),
        ('Auf der Vogelwiese 23 b', {'street': 'Auf der Vogelwiese', 'housenumber': '23 b'}),
        ('4, rue de la revolution', {'street': 'rue de la revolution', 'housenumber': '4'}),
        ('200, Broadway Av', {'street': 'Broadway Av', 'housenumber': '200'}),
        ('Calle Aduana, 29', {'street': 'Calle Aduana,', 'housenumber': '29'}),
        ('Calle 39 No 1540', {'street': 'Calle 39', 'housenumber': 'No 1540'}),
    ]

    _parse_addresses(addresses)


def test_parsing_no_house_number():
    addresses = [
        ('Dubai UAE', {'street': 'Dubai UAE', 'housenumber': ''}),
    ]

    _parse_addresses(addresses)


def test_parsing_no_street():
    addresses = [
        ('No 110', {'street': '', 'housenumber': 'No 110'}),
    ]

    _parse_addresses(addresses)


def test_numeric_only_house_number():
    addresses = [
        ('Winterallee 3', {'street': 'Winterallee', 'housenumber': '3'}),
        ('Musterstrasse 4', {'street': 'Musterstrasse', 'housenumber': '4'}),
        ('Am Bächle 23', {'street': 'Am Bächle', 'housenumber': '23'}),
        ('4, rue de la revolution', {'street': 'rue de la revolution', 'housenumber': '4'}),
        ('200, Broadway Av', {'street': 'Broadway Av', 'housenumber': '200'}),
        ('Calle Aduana, 29', {'street': 'Calle Aduana,', 'housenumber': '29'}),
    ]

    _parse_addresses(addresses)


def test_alphanumeric_house_number():
    addresses = [
        ('Blaufeldweg 123b', {'street': 'Blaufeldweg', 'housenumber': '123b'}),
        ('Auf der Vogelwiese 23 b', {'street': 'Auf der Vogelwiese', 'housenumber': '23 b'}),
        ('Calle 39 No 1540', {'street': 'Calle 39', 'housenumber': 'No 1540'}),
    ]

    _parse_addresses(addresses)


def test_house_number_contain_no():
    addresses = [
        ('Calle 39 No 1540', {'street': 'Calle 39', 'housenumber': 'No 1540'}),
    ]

    _parse_addresses(addresses)


def _parse_addresses(addresses):
    for address, valid_parsed_parts in addresses:
        assert AddressParser.normalize_address(address) == (
            valid_parsed_parts['housenumber'], valid_parsed_parts['street'])
