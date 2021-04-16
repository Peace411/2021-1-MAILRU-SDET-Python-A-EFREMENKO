import logging
from typing import Any
import json
import requests

logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 500


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.id_company = None
        self.base_url = base_url
        self.session = requests.Session()

        self.csrf_token = None
        self.id_segment = None

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

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=False,
                 allow_redirects=False):
        url = location

        self.log_pre(method, url, headers, data, expected_status)
        response = self.session.request(method, url, headers=headers, data=data, allow_redirects=allow_redirects)
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

    def get_token(self):
        location = 'https://target.my.com/csrf/'
        self._request('GET', location)
        csrftoken = self.session.cookies['csrftoken']
        self.csrf_token = csrftoken
        return csrftoken

    def post_login(self, user, password):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        self._request('GET', location, expected_status=302)

        headers = {
            'Host': 'auth-ac.my.com',
            'Origin': 'https://target.my.com',
            'Connection': 'keep-alive',
            'Referer': 'https://target.my.com/',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': 'Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.114 Safari/537.36 '

        }

        data = {
            'login': user,
            'password': password,
            'continue': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            'failure': "https://account.my.com/login/"

        }

        result = self._request('POST', location, headers=headers, expected_status=302, data=data, allow_redirects=False,
                               jsonify=False)
        self._request('GET', 'https://target.my.com/auth/mycom?state=target_login=1&ignore_opener=1',
                      expected_status=302)
        location = 'https://auth-ac.my.com/sdc?from=https://target.my.com/auth/mycom?state=target_login%3D1' \
                   '%26ignore_opener%3D1 '
        location = self._request('GET', location=location, expected_status=302).headers['location']

        self._request('GET', location, expected_status=302)
        self._request('GET', 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1')
        self._request('GET', 'https://target.my.com/', expected_status=302)
        self._request('GET', 'https://target.my.com/dashboard')

        self.get_token()
        return result

    def delete_segment(self, id_segment=None):
        if id_segment is None:
            id_segment = self.id_segment

        location = f'https://target.my.com/api/v2/remarketing/segments/{id_segment}.json'
        headers: dict[str, Any] = {
            'X-CSRFToken': self.csrf_token
        }
        self._request('DELETE', location=location, headers=headers, expected_status=204)

    def create_segment(self):
        location = 'https://target.my.com/api/v2/remarketing/segments.json'

        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/javascript, */*; q=0.01'

        }

        params = {
            "logicType": "or",
            "name": "test",
            "pass_condition": 1,
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "left": 365,
                        "right": 0,
                        "type": "positive"
                    }
                }
            ]
        }
        res = self._request('POST', location, headers=headers, data=json.dumps(params))
        id_segment = res.json()['id']
        self.id_segment = id_segment

    def create_company(self):
        location = 'https://target.my.com/api/v2/campaigns.json'
        headrs = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'

        }
        res = self._request('POST', location=location, headers=headrs, data=json.dumps(params_company))
        id_company = res.json()['id']
        self.id_company = id_company

    def delete_company(self, id_company=None):
        location = 'https://target.my.com/api/v2/campaigns/mass_action.json'
        if id_company is None:
            id_company = self.id_company
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'
        }
        params = [
            {
                "id": id_company,
                "status": "deleted"
            }
        ]
        self._request('POST', location=location, headers=headers, data=json.dumps(params), expected_status=204)


params_company = {
    "audit_pixels": [],
    "autobidding_mode": "fixed",
    "banners": [
        {
            "content": {
                "icon_256x256": {
                    "id": 8640939
                },
                "video_landscape_30s": {
                    "id": 8643100
                }
            },
            "name": "",
            "textblocks": {
                "cta_sites_full": {
                    "text": "visitSite"
                },
                "text_40": {
                    "text": "HI"
                },
                "title_25": {
                    "text": "HI"
                }
            },
            "urls": {
                "primary": {
                    "id": 1852176
                }
            }
        }
    ],
    "enable_utm": True,
    "max_price": "0",
    "mixing": "fastest",
    "name": "Новая кампания 16.04.2021 17:18:02",
    "objective": "general_ttm",
    "package_id": 560,
    "price": "1",
    "targetings": {
        "age": {
            "age_list": [
                0, 12
            ],
            "expand": True
        },
        "fulltime": {
            "flags": [
                "use_holidays_moving",
                "cross_timezone"
            ],
            "fri": [
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            ]

        },
        "geo": {
            "regions": [
                188
            ]
        },
        "interests": [],
        "interests_soc_dem": [],
        "pads": [
            39269,
            39270
        ],
        "segments": [],
        "sex": [
            "male",
            "female"
        ],
        "split_audience": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]
    },
    "uniq_shows_period": "day",
}
