import logging
from urllib.parse import urljoin
import requests


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 500


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.cookie = None
        self.session = requests.Session()

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    @property
    def post_headers(self):
        return {'Content-Type': 'application/json'}

    def _request(self, method, location, headers=None, expected_status=200, jsonify=True, **kwargs):
        data = kwargs.get('json', None) if kwargs.get('data', None) is None else kwargs.get('data')
        url = urljoin(self.base_url, location)
        self.log_pre(method, url, headers, data, expected_status)  # Method for logger
        if "json" in kwargs.keys():
            response = self.session.request(method, url, headers=headers, json=data, allow_redirects=False)
        else:
            response = self.session.request(method, url, headers=headers, data=data, allow_redirects=False)
        self.log_post(response)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.')
        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response.get('bErrorMsg', 'Unknown')
                raise ResponseErrorException(f'Request "{url}" return error "{error}"!')
            return json_response
        return response

    def get_status(self):
        location = '/status'
        return self._request('GET', location)

    def post_login(self, username, password, submit='Login', expected_status=302):
        location = '/login'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"username": username, "password": password, "submit": submit}
        result = self._request('POST', location=location, headers=headers, data=data, expected_status=expected_status,
                               jsonify=False)
        try:
            response_cookies = result.headers['Set-Cookie'].split(';')
            print(result.headers)
        except Exception as e:
            raise InvalidLoginException(e)
        self.cookie = response_cookies[0]
        return result

    def post_add_user(self, username, password, email, expected_status=201):
        location = '/api/add_user'
        headers = {"Content-Type": "application/json"}
        data = {"username": username, "password": password, "email": email}
        result = self._request('POST', location=location, headers=headers, json=data, expected_status=expected_status)
        return result

    def get_delete_user(self, username, expected_status=204):
        location = f'/api/del_user/{username}'
        result = self._request('GET', location=location, headers=None, json=None, expected_status=expected_status,
                               jsonify=False)
        return result

    def get_block_user(self, username, expected_status=200):
        location = f'/api/block_user/{username}'
        result = self._request('GET', location=location, headers=None, json=None, expected_status=expected_status,
                               jsonify=False)
        return result

    def get_find_me(self, expected_status=200):
        location = '/static/scripts/findMeError.js'
        result = self._request('GET', location=location, headers=None, data=None,
                               expected_status=expected_status)
        return result
    def get_unblock_user(self, username, expected_status=200):
        location = f'/api/accept_user/{username}'
        result = self._request('GET', location=location, headers=None, json=None,
                               expected_status=expected_status, jsonify=False)
        return result

    def post_registration(self, username, password, email, confirm, term='y', submit='Register', expected_status=302):
        location = '/reg'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"username": username, "email": email, "password": password,
                "confirm": confirm, "term": term, "submit": submit}
        result = self._request('POST', location=location, headers=headers, data=data,
                               expected_status=expected_status, jsonify=False)
        return result

    def get_logout(self, expected_status=302):
        location = '/logout'
        result = self._request('GET', location=location, headers=None, data=None,
                               expected_status=expected_status, jsonify=False)
        return result
