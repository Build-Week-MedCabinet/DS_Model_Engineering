import requests
import json
import sys

import predictor


# SETUP PARAMETERS
application_url = 'http://192.168.43.147:5000/'  # Changes/host.  Default on local to 127.0.0.1:80


# PAYLOADS
payloads = [
    {'search_params': 'random strings, some stuff, some more stuff'},
    """
    nice cherry is an indica-dominant strain that captures the flavorful
    qualities of its cherry parent and the relaxing attributes of mr. nice. with an aroma
    of sweet skunk, pine, and berry, nice cherry delivers a rush of cerebral energy
    that lifts the mood while relaxing the body. it’ll also bring an edge back to your
    appetite while providing focus to keep you productive.
    """,
    {'fake_flavor': 'fruity'},
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
predictor = predictor.Predictor()
predictor.transform(payloads[1])
print(predictor.predict())
