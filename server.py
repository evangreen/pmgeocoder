# Provides a simple HTTP server

from api import handle_api_request
from settings import gcsettings

# Python 2
try:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from urlparse import urlparse, parse_qs
    from urllib import urlencode

# Python 3
except ImportError:
    from urllib.parse import urlparse, urlencode, parse_qs
    from http.server import HTTPServer, BaseHTTPRequestHandler

# Create a basic server that response to GET requests.
class GeocoderTestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        result, data = handle_api_request(parsed_path.path,
                                          parse_qs(parsed_path.query))

        if gcsettings["debug"]:
            print("%d - %s" % (result, data))

        self.send_response(result)
        if result == 200:
            self.send_header("Content-type", "application/json")

        self.end_headers()
        self.wfile.write(data)

# Serve requests forever.
def serve():
    httpd = HTTPServer((gcsettings["server_host"], gcsettings["server_port"]),
                       GeocoderTestHTTPRequestHandler)

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        pass

    httpd.server_close()
    return

if __name__ == '__main__':
    print("Serving requests on %s at port %d" %
          (gcsettings["server_host"], gcsettings["server_port"]))

    if gcsettings["debug"]:
        print("Debug mode is active")

    if gcsettings["hereapi"]["app_id"][:4] == "FILL" or \
       gcsettings["googlemaps"]["api_key"][:4] == "FILL":

       print("Warning: You need to edit settings.py and fill in your API keys.")

    serve()
    print("Goodbye")
