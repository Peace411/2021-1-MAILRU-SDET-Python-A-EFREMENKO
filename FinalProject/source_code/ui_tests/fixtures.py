import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from ui_tests.pages.base_page import BasePage
from ui_tests.pages.main_page import MainPage
from ui_tests.pages.login_page import LoginPage


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


@pytest.fixture(scope='session')
def base_temp_dir():
    base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir


def get_driver(browser_name, download_dir):
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option("prefs", {"download.default_directory": download_dir})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise UnsupportedBrowserType(f' Unsupported browser {browser_name}')

    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    browser_name = config['browser']

    browser = get_driver(browser_name, download_dir=temp_dir)

    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request, temp_dir):
    url = config['url']

    browser = get_driver(request.param, download_dir=temp_dir)

    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()