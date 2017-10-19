# This module responds to API requests.

from geocoder import address_to_lat_long
from json import dumps

# Define the current API version.
API_VERSION = "v1"

# Helper function to send an error response in JSON
def send_error_response(message):
    response = {
        "error": message
    }

    return 200, dumps(response)

# Function to handle address to lat/long requests
def handle_address_request(params):
    for key in ["address"]:
        try:
            params[key][0];

        except KeyError:
            return send_error_response("Expected parameter %s" % key)

    address = params["address"][0]
    lat, long = address_to_lat_long(address)
    if lat is None:
        return send_error_response("Address not found")

    response = {
        "data": {
            "address": address,
            "latitude": lat,
            "longitude": long
        }
    }

    return 200, dumps(response)

# Define the various endpoints.
endpoints = {
    "address": handle_address_request
}

# Generic function to handle an API request, given a path and a set of GET
# or POST parameters
def handle_api_request(path, params):
    paths = path.split('/')
    if len(paths) != 3:
        return 404, "Invalid request path"

    if paths[1] != API_VERSION:
        return 404, "Unknown API version"

    handler_name = paths[2]
    if handler_name[-5:] != ".json":
        return 404, "Unknown format"

    handler_name = handler_name[:-5]
    try:
        handler = endpoints[handler_name]
        return handler(params)

    except KeyError:
        pass

    return 404, "Unknown endpoint"
