import logging
import json


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
        data = request.query_params
        logger.info(
            request.data, request.content_type, request.query_params
            )
    print(data)
    return data
