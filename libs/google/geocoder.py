import urllib.parse
from requests import get
from pprint import pprint


class GoogleAPI:
    def __init__(self):
        self.API_KEY = 'GOOGLE_API_KEY'
        self.URL = 'https://maps.googleapis.com/maps/api/geocode/json?components=&language=&region=&bounds=&key={}&address={}'

    def get_address_details(self, address):
        house_number = ''
        street = ''

        if address:
            final_url = self.URL.format(
                self.API_KEY,
                urllib.parse.quote_plus(address)
            )
            response = get(final_url)
            resolved_address = self.address_resolver(response.json())
            house_number = resolved_address.get('housenumber', '')
            street = '{} {}'.format(
                resolved_address.get('street_number', ''),
                resolved_address.get('street', ''),
            )

        return house_number, street

    def address_resolver(self, json):
        final = {}
        if json.get('results', None):
            data = json['results'][0]
            for item in data['address_components']:
                for category in item['types']:
                    data[category] = {}
                    data[category] = item['long_name']
            final['street'] = data.get("route", None)
            final['state'] = data.get("administrative_area_level_1", None)
            final['city'] = data.get("locality", None)
            final['county'] = data.get("administrative_area_level_2", None)
            final['country'] = data.get("country", None)
            final['postal_code'] = data.get("postal_code", None)
            final['neighborhood'] = data.get("neighborhood", None)
            final['sublocality'] = data.get("sublocality", None)
            final['housenumber'] = data.get("housenumber", None)
            final['postal_town'] = data.get("postal_town", None)
            final['subpremise'] = data.get("subpremise", None)
            final['latitude'] = data.get("geometry", {}).get("location", {}).get("lat", None)
            final['longitude'] = data.get("geometry", {}).get("location", {}).get("lng", None)
            final['location_type'] = data.get("geometry", {}).get("location_type", None)
            final['postal_code_suffix'] = data.get("postal_code_suffix", None)
            final['street_number'] = data.get('street_number', None)

        return final
