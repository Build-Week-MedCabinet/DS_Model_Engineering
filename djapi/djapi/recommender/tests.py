import requests
import json
import sys
import time
import faker
import timeit

import predictor


# SETUP PARAMETERS
# PARAMETERS
params = {
    'devURL': 'http://192.168.43.147:5000/', # Changes/host.  Default on local to 127.0.0.1:80
    'prodURL': 'https://morning-badlands-32563.herokuapp.com',
}

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
url = params['prodURL']+'recommend'
try:
    r = requests.get(url, payloads[0])
    print('URL: ', r.url)
except:
    print("Unexpected error:", sys.exc_info()[0])

try:
    print('JSON: ', r.json())
except:
    print('JSON request error.')

try:
    print('Text:', r.text)
except:
    print('Text request error.')

# Test 2
# check Predictor class makes, can return result from dummy data (library test local only)
rec_engine = predictor.Predictor()
rec_engine.transform(payloads[1])
print('Library Prediction', rec_engine.predict())

# Check Get_Recommendation utility to see if data from csv can be returned (library test local only)
print('Recommendation:', rec_engine.get_recommendation())


# Test 3
# Test repeated calls and time each one (library test local only)
def call_api(size=5):
    engine = predictor.Predictor()
    engine.transform(get_payload())
    return engine.get_recommendation()


def get_payload():
    generator = faker.Faker()
    generator.add_provider('lorem')
    return generator.sentence(
        nb_words=6,
        variable_nb_words=True,
        ext_word_list=None
        )

request_interval = .1
total_requests = 10
request_times = []
for i in range(total_requests):
    print('run: ', i)
    request_times.append(
        timeit.timeit(call_api, number=1)
    )
    time.sleep(request_interval)

print(
    'Request Intervals for {} requests/s, total {} \
    requests:\n {}'.format(1/request_interval, total_requests, request_times)
    )
