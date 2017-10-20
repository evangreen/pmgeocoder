# This module implements the generic backend interface. It is extended
# for particular backends.

import codecs
from json import loads
from settings import gcsettings

# Python 3
try:
    from urllib.request import urlopen

# Python 2
except ImportError:
    from urllib2 import urlopen

# Encapsulate an API response into an object so that potentially multiple
# answers can be satisfied in the future with a single response, or maybe even
# be cached.
class GeocoderBackendResponse:
    code = 0
    raw = ""
    data = {}

# Define the parent backend class.
class GeocoderBackend:

    # This helper method is used by the child classes to actually perform a
    # basic JSON API call. They are not required to use it.
    def _json_api_request(self, url, data):
        request = urlopen(url, data, gcsettings["timeout"])
        response = GeocoderBackendResponse()
        response.code = request.getcode()
        reader = codecs.getreader("utf-8")
        response.raw = reader(request).read()
        response.data = loads(response.raw)
        return response
