#!/bin/bash
# Script takes in a URL as an argument, sends a GET request to the URL,and displays the body of the response(including header x-school-user-id with value of 98)
curl -sH "X-School-User-Id: 98" "$1"
