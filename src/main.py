import http.server
import random
import time
from prometheus_client import start_http_server, Counter, Summary

REQUESTS = Counter('hello_worlds_total',
        'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_world_exceptions_total',
        'Exceptions serving Hello World.')
LATENCY = Summary(
    'hello_world_latency',
    'Time taken by the request'
)

class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time()
    def do_GET(self):
        REQUESTS.inc()
        with EXCEPTIONS.count_exceptions():
          if random.random() < 0.1:
            raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('0.0.0.0', 8001), MyHandler)
    server.serve_forever()