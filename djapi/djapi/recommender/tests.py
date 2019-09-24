import requests
import json
import sys

# SETUP PARAMETERS
application_url = 'http://192.168.43.147:5000/'  # Changes/host.  Default on local to 127.0.0.1:80


# PAYLOADS
payloads = [
    {'search_params': 'random strings, some stuff, some more stuff'},
    {}
]



# Test 1
# check that api responds to get request and returns request.
print('Running Test {} with payload {}'.format(1, payloads[0]))
url = application_url+'recommend'
try:
    r = requests.get(url, payloads[0])
    print('URL: ', r.url)
    print('JSON: ', r.json())
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# Test 2
# check Predictor class makes, can return result from dummy data

