import logging
import socket
import json
import time

from mock.flask_mock import mock_data
import settings

user_id_seq = 1

logger = logging.getLogger('client')
class HttpClient:

    def __init__(self):
        self.host = settings.MOCK_HOST
        self.port = int(settings.MOCK_PORT)
        self.client = None

    def connect_http_client(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.settimeout(0.1)
        client.connect((self.host, self.port))
        self.client = client

    def get_user(self, name):
        params = f'/get_user_name/{name}'

        data = self.send_request(request_type="GET", params=params)

        return data

    def send_request(self, request_type, params, data=None):
        self.connect_http_client()

        request = f"{request_type} {params}  HTTP/1.1\r\nHost: {self.host}\r\n"
        if data:
            body = f"Content-Type: application/json\r\nContent-Length: {str(len(data))}\r\n\r\n{data}"
            req = request + body
            self.client.send(req.encode())
        else:
            request += '\r\n'
            self.client.send(request.encode())

        res = self.client_recv
        logger.info(f'request {request_type} on {params},server response: {res} ')
        return res

    def post_user(self, name):
        params = f'/post_name'
        m = {'name': name}
        data = json.dumps(m)
        request = self.send_request(request_type='POST', params=params, data=data)
        return request

    def get_user_surname(self, name):
        params = f'/get_surname/{name}'
        request = self.send_request(request_type='GET', params=params)
        return request

    def post_surname(self, name, surname):
        params = f'/post_surname/{name}'
        m = {'surname': surname}
        data = json.dumps(m)

        request = self.send_request(request_type='POST', params=params, data=data)
        return request

    def put_surname(self, name, surname):
        params = f'put_surname/{name}'
        m = {'surname': surname}
        data = json.dumps(m)
        request = self.send_request(request_type='PUT', params=params, data=data)
        return request

    def delete_surname(self, name, surname):
        params = f'delete_surname/{name}'
        m = {'surname': surname}
        data = json.dumps(m)
        requests = self.send_request(request_type='DELETE', params=params, data=data)
        return requests

    @property
    def client_recv(self):
        total_data = []
        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.client.close()
                break

        data = ''.join(total_data).splitlines()
        return data
