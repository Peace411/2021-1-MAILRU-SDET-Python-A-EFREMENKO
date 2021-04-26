import json
import logging
import os
from typing import Any

import requests
from faker import Faker

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
        self.base_url = base_url
        self.session = requests.Session()

        self.csrf_token = None

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

        headers = {
            'Referer': 'https://target.my.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'login': user,
            'password': password,
            'continue': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            'failure': "https://account.my.com/login/"

        }

        result = self._request('POST', location, headers=headers, expected_status=200, data=data, allow_redirects=True,
                               jsonify=False)
        self.get_token()
        return result

    def delete_segment(self):
        id_segment = self.create_segment()
        location = f'https://target.my.com/api/v2/remarketing/segments/{id_segment}.json'
        headers: dict[str, Any] = {
            'X-CSRFToken': self.csrf_token
        }
        self._request('DELETE', location=location, headers=headers, expected_status=204)

    def upload_files(self):
        image = os.path.abspath(os.path.join(os.path.dirname(__file__), 'stuff/381D0F.jpg'))
        im = open(image, 'rb')
        video = os.path.abspath(os.path.join(os.path.dirname(__file__), 'stuff/51740A.mp4'))
        video_heders = {
            'X-CSRFToken': self.csrf_token
        }
        video_data = {
            'height': '720',
            'width': '1280',
        }
        files_video = {'file': open(video, 'rb')}
        image_headers = {
            'X-CSRFToken': self.csrf_token
        }
        files = {'file': im}
        image_data = {
            'height': '256',
            'width': '256',
        }

        location = 'https://target.my.com/api/v2/content/static.json'
        image = self.session.post(location, headers=image_headers, data=image_data, files=files)
        location = 'https://target.my.com/api/v2/content/video.json'
        video = self.session.post(location, headers=video_heders, data=video_data, files=files_video)
        id_video = video.json()['id']
        id_image = image.json()['id']
        return id_image, id_video

    def create_segment(self):
        fake = Faker()
        location = 'https://target.my.com/api/v2/remarketing/segments.json'

        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/javascript, */*; q=0.01'

        }
        params = {
            "logicType": "or",
            "name": fake.lexify(text='?? ?? ??? ??????'),
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
        return id_segment

    def create_company(self):
        fake = Faker()
        id_stuff = self.upload_files()
        location = 'https://target.my.com/api/v2/campaigns.json'
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'

        }
        params_company = {
            "audit_pixels": [],
            "autobidding_mode": "fixed",
            "banners": [
                {
                    "content": {
                        "icon_256x256": {
                            "id": id_stuff[0]
                        },
                        "video_landscape_30s": {
                            "id": id_stuff[1]
                        }
                    },
                    "name": fake.lexify(text='?? ?? ??? ??????'),
                    "textblocks": {
                        "cta_sites_full": {
                            "text": "visitSite"
                        },
                        "text_40": {
                            "text": fake.lexify(text='?? ?? ??? ??????')
                        },
                        "title_25": {
                            "text": fake.lexify(text='?? ?? ??? ??????')
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
            "name": fake.lexify(text='?? ?? ??? ??????'),
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
                "split_audience": [
                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                ]
            }
        }
        res = self._request('POST', location=location, headers=headers, data=json.dumps(params_company))
        id_company = res.json()['id']
        self.delete_company(id_company=id_company)
        return id_company

    def delete_company(self, id_company=None):
        location = 'https://target.my.com/api/v2/campaigns/mass_action.json'

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
