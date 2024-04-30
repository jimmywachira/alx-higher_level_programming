#!/bin/bash
# Script sends request to particular URL and get the byte size of the HTTP response header.
curl -s "$1" | wc -c
