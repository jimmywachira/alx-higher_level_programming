#!/usr/bin/python3
"""
sript takes in url, sneds a request to the url and
displays value of variable x-request-d in response header
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
