# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:31:53 2024

@author: giuli
"""

import http.server
import socketserver
import os
import http.cookies
import base64

port = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.exists(path):
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        with open('post_data.log', 'a') as f:
            f.write(post_data.decode('utf-8') + '\n')
    
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'POST ricevuta con successo')
    
def do_AUTH(self):
    user_credentials = {
        "admin": "password123",
        "user": "securepassword"
    }

    auth_header = self.headers.get('Authorization')
    if auth_header:
        auth_data = auth_header.split(' ')
        if len(auth_data) == 2 and auth_data[0].lower() == 'basic':
            username_password = auth_data[1].encode('utf-8')
            decoded_credentials = base64.b64decode(username_password).decode('utf-8')
            username, password = decoded_credentials.split(':', 1)

            if username in user_credentials and user_credentials[username] == password:
                return True

    self.send_response(401)
    self.send_header('WWW-Authenticate', 'Basic realm="Accesso protetto"')
    self.end_headers()
    self.wfile.write(b'Autenticazione richiesta')
    return False


    def do_SESSION(self):
        cookie = http.cookies.SimpleCookie(self.headers.get('Cookie'))
        if 'session_id' not in cookie:
            session_id = os.urandom(16).hex()
            self.send_header('Set-Cookie', 'session_id=' + session_id)
            self.end_headers()
        else:
            session_id = cookie['session_id'].value
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'Session ID: {session_id}'.encode('utf-8'))

with socketserver.ThreadingTCPServer(("", port), CustomHTTPRequestHandler) as httpd:
    print("Server avviato sulla porta", port)
    httpd.serve_forever()
