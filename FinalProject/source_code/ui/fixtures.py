import os
import shutil
import socket

import allure
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from api_client.client import ApiClient
from mysql_client.builder import MySQLBuilder
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage
from ui.pages.registration_page import RegistrationPage

fake = Faker()


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver=driver)


@pytest.fixture(scope='function')
def cookies(config, mysql_client):
    mysql = MySQLBuilder(mysql_client)
    test_user = mysql.create_test_user()
    login_page = LoginPage(driver)
    login_page.user_login(test_user.username, test_user.password)
    cookies = driver.get_cookies()
    return cookies


@pytest.fixture(scope='session')
def base_temp_dir():
    base_dir = '/tmp/ui_tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture()
def get_user(mysql_client):
    mysql = MySQLBuilder(mysql_client)
    test_user = mysql.create_test_user()
    username = test_user.username
    password = test_user.password
    email = test_user.email
    return username, password,email



def get_driver(config, download_dir):
    browser_name = config['browser']

    if browser_name == 'chrome':
        options = ChromeOptions()
        options.set_capability("browserVersion", "89.0")
        caps = {'browserName': browser_name,
                'version': '89.0'}

        browser = webdriver.Remote(command_executor=f"http://{socket.gethostbyname('selenoid')}:4444/wd/hub",
                                   options=options, desired_capabilities=caps)

    else:
        raise UnsupportedBrowserType(f' Unsupported browser {browser_name}')

    return browser


@pytest.fixture(scope='function')
def driver(config, test_dir):
    url = config['url']
    browser = get_driver(config, download_dir=test_dir)
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)
