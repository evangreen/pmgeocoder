# This module implements the generic backend interface. Its methods are
# overridden for a particular backend.

from json import loads
from settings import gcsettings

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

class GeocoderBackendResponse:
    code = 0
    raw = ""
    data = {}

class GeocoderBackend:
    def _json_api_request(self, url, data):
        request = urlopen(url, data, gcsettings["timeout"])
        response = GeocoderBackendResponse()
        response.code = request.getcode()
        response.raw = request.read()
        response.data = loads(response.raw)
        return response
