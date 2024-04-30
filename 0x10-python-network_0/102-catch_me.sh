#!/bin/bash
# Bash script makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!"as response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
