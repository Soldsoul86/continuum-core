import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from continuum_core.event_store import read_events


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/events":
            events = read_events()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")

            # CORS: allow read-only access from UI
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET")
            self.send_header("Access-Control-Allow-Headers", "*")

            self.end_headers()
            self.wfile.write(json.dumps(events).encode())
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    print("Continuum core listening on http://localhost:8000")
    HTTPServer(("localhost", 8000), Handler).serve_forever()

