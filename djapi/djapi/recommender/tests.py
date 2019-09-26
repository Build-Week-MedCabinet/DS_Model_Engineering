import requests
import json
import os
import sys
import datetime
import faker
import time
import timeit

# import predictor  # Required for tests 1, 2, 3.  Imports fail with caching framework.


# SETUP PARAMETERS
# PARAMETERS
params = {
    'devURL': 'http://192.168.43.147:5000/', # Changes/host.  Default on local to 127.0.0.1:80
    'prodURL': 'https://morning-badlands-32563.herokuapp.com/',
    'log': 'tests/test_log.txt'
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


# Log function

def log(message):
    def write_message(message, f):
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        if type(message) == list:
            for log_item in message:
                f.write(time_str+': ')
                f.write(log_item+'\n')
        elif type(message) == str:
            f.write(time_str+': ')
            f.write(message+'\n')

    if os.path.isfile(params['log']):
        with open(params['log'], 'a+') as f:
            write_message(message, f)
    else:
        with open(params['log'], 'w+') as f:
            write_message(message, f)



# Test 1
# check that api responds to get request and returns request.
def run_test_1(stage):
    print('Running Test {} with payload {}'.format(1, payloads[0]))
    url = params[stage+'URL']+'recommend'
    print('Test URL: ', url)
    try:
        r = requests.get(url, payloads[0])
        log('Test_url'+r.url)
        print(stage, r.url)
    except:
        log(["Unexpected error:", sys.exc_info()[0]])
        raise

    try:
        if r.json:
            log([stage, str(r.json)])
            print('Json data available. JSON data returned!')
    except:
        print('JSON request error.')
        raise

    try:
        if r.text:
            log([stage, str(r.text)])
            print('Text data available. Request data returned!')
    except:
        print('Text request error.')
        raise

# Test 2
# check Predictor class makes, can return result from dummy data (library test local only)
def run_test_2(output=False):
    rec_engine = predictor.Predictor()
    rec_engine.transform(payloads[1])
    log(['library_test predict', '-'.join(
        [str(x) for x in rec_engine.predict()])
        ])
    if output:
        print('Library Prediction', rec_engine.predict())

    # Check Get_Recommendation utility to see if data from csv can be returned (library test local only)
    log(['library_test recommendation', rec_engine.get_recommendation()])
    if output:
        print('Recommendation:', rec_engine.get_recommendation())


# Test 3
# Test repeated calls and time each one (library test local only)
def call_local_library(size=5):
    engine = predictor.Predictor()
    engine.transform(get_payload())
    recommendation = engine.get_recommendation()
    log(['test_3 run', engine.raw_input, recommendation])
    return recommendation


def get_payload():
    generator = faker.Faker()
    generator.add_provider('lorem')
    return generator.sentence(
        nb_words=7,
        variable_nb_words=True,
        ext_word_list=None
        )

request_interval = .1
total_requests = 10
request_times = []

def run_local_time_test():
    for i in range(total_requests):
        print('run: ', i)
        request_times.append(
            timeit.timeit(call_local_library, number=1)
        )

    print(
        'Request Intervals for {} requests/s, total {} \
        requests:\n {}'.format(1/request_interval, total_requests, request_times)
        )

def run_test_3():
    run_local_time_test()


# Test 4 similar to test 3 only on the production side
def call_api(stage='prod', log_message="Test_4"):
    url = params[stage+'URL']+'recommend'
    payload = get_payload()
    r = requests.get(url, payload)
    recommendation = r.text
    log([log_message+' '+stage, payload, recommendation])
    return recommendation


def call_api_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def run_test_4(stage='prod', total_requests=5, request_interval=0.05):
    request_times = []
    try:

        for i in range(total_requests):
            print('Test 4, run: ', i)
            call_api_function = call_api_wrapper(func=call_api, stage=stage)
            request_times.append(
                timeit.timeit(call_api_function, number=1)
            )
            time.sleep(request_interval)

        print(
            'Request Intervals for {} requests/s, total {} \
            requests:\n {}'.format(
                1/request_interval, total_requests, request_times))
    except:
        log('Error in Test 4')
        print('Errot in Test 4')
        raise
    return 'Test 4 Complete'


if __name__ == "__main__":
    # run_test_1('dev')
    # run_test_1('prod')
    # run_test_2()
    # run_test_3()
    run_test_4(stage='dev')
    run_test_4(stage='prod')
