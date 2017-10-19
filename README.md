# Geocoding Proxy

This repository implements a simple Geocoding API, using Google Maps or here.com
as a data source.

### Running the service
The service can be started by running `python server.py`. This will fire up a
basic HTTP server that will serve requests forever. Configuration information
is specified in the settings.py file.

There is a single environment variable that is queried: "DEBUG". If this is set
to anything not empty, then debug settings will be used. Otherwise, production
settings will be used.

### Configuring the service
The file settings.py contains the admin-configurable portions of the service.
This includes the server host and port number, as well as API keys for the
supported data services. You will need to fill in your API keys.

The rest of the service accesses the gcsettings variable to get at
configuration data. The settings module can be swapped out for some sort of
automated configuration management tool with hopefully minimal hassle.

### API
JSON data is sent in response to an HTTP GET request in the form:

http://example.com/v1/address.json?address=Chicago

Responses to other URLs will result in failing HTTP status codes. Otherwise,
the server will respond with a JSON formatted message. A successful response
will contain the original address query, a latitude, and a longitude, like this:

{
    "data": {
        "latitude": 41.8781136,
        "longitude": -87.6297982,
        "address": "Chicago"
    }
}

A failing result, either because of an invalid input parameter, the given
address could not be found in any of the data sources, or no data sources were
reachable, contains an error response, like this:

{
    "error": "Message explaining the error. Commonly Address not found"
}
