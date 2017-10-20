from settings import gcsettings
from backend import GeocoderBackend
import pprint

# Python 2
try:
    from urllib import urlencode

# Python 3
except ImportError:
    from urllib.parse import urlencode

BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

class GoogleGeocoderBackend(GeocoderBackend):
    name = "Google Maps"
    def __init__(self):
        self.api_key = gcsettings["googlemaps"]["api_key"]
        self.debug = gcsettings["debug"]
        return

    # Execute an API request searching for a given free-form address, and return
    # a GeocoderBackendResponse object.
    def lookup_address(self, address):
        qs = urlencode({'api_key': self.api_key, 'address': address})
        url = "%s?%s" % (BASE_URL, qs)
        if self.debug:
            print("Making %s API request: %s" % (self.name, url))

        response = self._json_api_request(url, None)
        response.query = address
        if (gcsettings["debug"]):
            print("%d Response from %s:" % (response.code, self.name))
            pprint.pprint(response.data)

        return response

    # Given a geocoder backend response object, get a latitude and longitude
    # from it.
    def lat_long(self, response):
        data = response.data
        results = data["results"]
        if len(results) == 0:
            return None, None

        location = results[0]["geometry"]["location"]
        return (location["lat"], location["lng"])
