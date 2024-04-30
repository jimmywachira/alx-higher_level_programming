#!/usr/bin/python3
"""script takes in a URL and an email address, 
sends a POST request to URL passed with the email as a parameter, 
utimately displays the body of the response.
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    print(req.text)
