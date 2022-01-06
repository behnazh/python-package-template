"""This is a deliberately vulnerable class for testing."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """This is a simple http request handler vulnerable to XSS."""

    def do_GET(self):  # pylint: disable-msg=C0103 # noqa: N802
        """Reflect the request path without sanitization."""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(self.path, "utf-8"))


httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
