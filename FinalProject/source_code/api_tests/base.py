import os
import pytest
import faker

from api_client.builder import ApiUserBuilder
from mysql_client.builder import MySQLBuilder
from mysql_client.models import TestUsers


class BaseCaseApi:  # Base Case Object API
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, client_api, mysql_client):
        self.client_api = client_api
        self.mysql_client = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)
        self.api_user_builder = ApiUserBuilder()
        self.main_user = self.mysql_builder.create_test_user()
        if self.authorize:
            self.do_authorize(username=self.main_user.username, password=self.main_user.password)
        yield

    def do_authorize(self, username, password):
        return self.client_api.post_login(username, password)

    def add_user(self, username, password, email):
        return self.client_api.post_add_user(username, password, email)

