import re


class AddressParser:

    @classmethod
    def normalize_address(cls, address):
        house_number = ''
        street = ''

        if address:
            matches = (re.findall(r'(No \d+|\d+[b]|\d+ [b]\b|\d+)', address))
            house_number = max(matches) if len(matches) else ''
            street = address.replace(house_number, '').strip(',;').strip()

        return house_number, street
