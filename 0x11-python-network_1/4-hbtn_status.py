#!/usr/bin/python3
"""
 script fetches https://alx-intranet.hbtn.io/status
 like 0-hbtn_status but using requests only
"""

import requests

if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
