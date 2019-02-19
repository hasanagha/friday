from libs.google.geocoder import GoogleAPI
from libs.streetaddress import StreetAddressParser

from libs.parser import AddressParser


if __name__ == '__main__':
    addr_parser = StreetAddressParser()

    addresses = [
        'Winterallee 3',
        'Musterstrasse 4',
        'Blaufeldweg 123b',

        'Am Bächle 23',
        'Auf der Vogelwiese 23 b',

        '4, rue de la revolution',
        '200, Broadway Av',
        'Calle Aduana, 29',
        'Calle 39 No 1540',
    ]

    for address in addresses:
        # Address parser using RegEx (Custom)
        house_number, street = AddressParser.normalize_address(address)

        # Using Geocoding API
        # house_number, street = GoogleAPI().get_address_details(address)

        # Using street address library (https://github.com/pnpnpn/street-address)
        # parsed_address = addr_parser.parse(address)
        # street = parsed_address.get('street_full')
        # house_number = parsed_address.get('house')

        print({
            'street': street,
            'housenumber': house_number
        })
