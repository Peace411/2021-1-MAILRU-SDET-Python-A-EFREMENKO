import socket

import pytest
from _pytest.fixtures import FixtureRequest

from api_client.builder import ApiUserBuilder
from mysql_client.builder import MySQLBuilder
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationPage


class BaseCase:
    authorize = True
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest,client_api,mysql_client,ui_report):
        self.driver = driver
        self.client_api =client_api
        self.config = config
        self.mysql_client = mysql_client
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.registr_page: RegistrationPage = request.getfixturevalue('registration_page')

        self.mysql = MySQLBuilder(self.mysql_client)
        if self.authorize:
            test_user = self.mysql.create_test_user()
            self.username = test_user.username
            self.password = test_user.password
            login_page = LoginPage(self.driver)
            login_page.user_login(test_user.username, test_user.password)
            self.driver.refresh()
            self.main_page = MainPage(driver)