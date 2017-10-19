# Settings module for the geocoder API. Fill in installation specific settings
# here.

import os

debugsettings = {
    # Set this to true to get console output for debugging
    "debug": True,

    # here.com API settings.
    "hereapi": {
        "app_id": "FILL_IN_YOUR_APP_ID",
        "app_code": "FILL_IN_YOUR_APP_CODE",
    },

    # Google Map API settings.
    "googlemaps": {
        "api_key": "FILL_IN_YOUR_API_KEY"
    },

    # Define the timeout in seconds to wait on each backend.
    "timeout": 5,

    # Local server bind host
    "server_host": "0.0.0.0",

    # Local server bind port
    "server_port": 8000,
}

productionsettings = {
    # Set this to true to get console output for debugging
    "debug": False,

    # here.com API settings.
    "hereapi": {
        "app_id": "FILL_IN_YOUR_APP_ID",
        "app_code": "FILL_IN_YOUR_APP_CODE",
    },

    # Google Map API settings.
    "googlemaps": {
        "api_key": "FILL_IN_YOUR_API_KEY"
    },

    # Define the timeout in seconds to wait on each backend.
    "timeout": 5,

    # Local server bind host
    "server_host": "0.0.0.0",

    # Local server bind port
    "server_port": 80,
}

# Use different settings if DEBUG is set in the environment.
if os.getenv("DEBUG"):
    gcsettings = debugsettings

else:
    gcsettings = productionsettings
