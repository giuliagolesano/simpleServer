# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:09:34 2024

@author: giuli
"""

import requests

server_url = "http://localhost:8000"

def test_post_method():
    url = server_url
    data = {"key": "value"}
    response = requests.post(url, data=data)
    print("Risposta dalla richiesta POST:", response.text)

def test_authentication():
    url = server_url
    username = "admin"
    password = "password123"
    auth = (username, password)
    response = requests.get(url, auth=auth)
    print("Risposta dall'autenticazione:", response.text)

def test_session_management():
    url = server_url
    response = requests.get(url)
    print("Risposta dalla gestione della sessione:", response.text)

if __name__ == "__main__":
    print("Test del metodo do_POST:")
    test_post_method()
    
    print("\nTest dell'autenticazione:")
    test_authentication()
    
    print("\nTest della gestione della sessione:")
    test_session_management()
