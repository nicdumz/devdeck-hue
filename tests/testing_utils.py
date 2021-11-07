import json
import os
from urllib.request import Request


class TestingUtils:
    @staticmethod
    def get_filename(relative_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

    @staticmethod
    def scrub_request(request: Request) -> Request:
        components = request.path.split('/')
        assert components[1] == 'api'
        components[2] = '__scrubbed_username__'
        request.uri = '/'.join(components)
        return request

    @staticmethod
    def scrub_response(response: Request) -> Request:
        data = json.loads(response['body']['string'])
        if isinstance(data, dict):
            for key in {'productid', 'swconfigid', 'swupdate', 'swversion', 'uniqueid'}:
                data.pop(key, None)
        response['body']['string'] = json.dumps(data).encode()
        return response