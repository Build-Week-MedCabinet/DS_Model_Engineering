import requests
import json

# SETUP PARAMETERS
application_url = 'http://192.168.43.147:5000/'  # Changes/host.  Default on local to 127.0.0.1:80


# PAYLOADS
payloads = [
    {'search_params': 'random strings, some stuff, some more stuff'}
]



# Test 1
# check that api responds to get request and returns request.
url = application_url+'recommend'
r = requests.get(url, payloads[0])
print('Running Test {} with payload {}'.format(1, json.dumps(payloads)))
print('URL: ', r.url)
print('JSON: ', r.json())
