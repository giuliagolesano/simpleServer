import http.server
import socketserver
import os

port = 8000

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.exists(path):
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')

with socketserver.ThreadingTCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
    print("Server avviato sulla porta", port)
    httpd.serve_forever()
