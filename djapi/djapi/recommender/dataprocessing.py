import logging
import json
import string


logger = logging.getLogger(__name__)


def process_request(request):
    """ Process request to string """
    if request.is_ajax():
        # print('ajax request found.') # Debug
        data = json.loads(request.body)
        logger.info(
            "ajax recieved: {}".format(data)
        )
    else:
        # print(request.data)  # Debug
        # print(request.content_type)  # Debug
        data = json.dumps(request.query_params)
        logger.info(
            request.data, request.content_type, request.query_params
            )
    print(type(data), data)
    data = strip_string(data)
    print(type(data), data)
    return data


def strip_string(data):
    if type(data) == str:
        return data.translate(str.maketrans('', '', string.punctuation))

    return data
