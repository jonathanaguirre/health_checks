#!/usr/bin/env python3
# health_checks.py uses this module
import requests
import socket
localhost = socket.gethostbyname('localhost')
request = requests.get("http://www.google.com")
response = request.status_code
def check_localhost():
        return localhost=="127.0.0.1"
def check_connectivity():
        return response==200
