# Geocoder backend for here.com.

from settings import gcsettings
from backend import GeocoderBackend
import pprint

# Python 2
try:
    from urllib import urlencode

# Python 3
except ImportError:
    from urllib.parse import urlencode

BASE_URL = "https://geocoder.api.here.com"
API_VERSION = "6.2"

class HereGeocoderBackend(GeocoderBackend):
    name = "here.com"
    def __init__(self):
        self.app_id = gcsettings["hereapi"]["app_id"]
        self.app_code = gcsettings["hereapi"]["app_code"]
        self.debug = gcsettings["debug"]
        return

    # Execute an API request searching for a given free-form address, and return
    # a GeocoderBackendResponse object.
    def lookup_address(self, address):
        qs = urlencode({'app_code': self.app_code,
                        'app_id': self.app_id,
                        'searchtext': address})

        url = "%s/%s/search.json?%s" % (BASE_URL, API_VERSION, qs)
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
        views = data["Response"]["View"]
        if len(views) == 0:
            return None, None

        location = views[0]["Result"][0]["Location"]
        pos = location["NavigationPosition"][0]
        return (pos["Latitude"], pos["Longitude"])
