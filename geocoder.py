# Provides the primary interface to the geocoding service.

from backends.here import HereGeocoderBackend
from backends.googlemaps import GoogleGeocoderBackend
from settings import gcsettings

# Define the available backends. This currently creates a single instance of
# each backend up front and reuses them. It could also easily be changed to
# store the types themselves, and have instances be created per request.
backends = [
    GoogleGeocoderBackend(),
    HereGeocoderBackend()
]

def address_to_lat_long(address):
    for backend in backends:
        try:
            response = backend.lookup_address(address)
            lat, long = backend.lat_long(response)
            if lat is not None:
                return (lat, long)

        # Ideally this should only catch specific exception types that the
        # framework is expecting, so as not to swallow arbitrary bugs in
        # backends, but due to limited time and the desire on the frontend to
        # make as much progress as possible, this catches all exceptions.
        except Exception as e:
            if gcsettings["debug"]:
                print("Backend %s generated exception: %s" % (backend.name, e))

    return None, None
