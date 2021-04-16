import os
import logging
import shutil
from webdriver_manager.chrome import ChromeDriverManager

import allure
import pytest
from selenium import webdriver

from api.api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--url', default='https://target.my.com/')

@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    return {'debug_log': debug_log,'url':url}

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.set_window_size(1024, 600)
    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()




def pytest_configure(config):
    base_test_dir = "/tmp/tests"

    if not hasattr(config, 'workerinput'):  # execute only once on main worker
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    # save to config for all workers
    config.base_test_dir = base_test_dir


@pytest.fixture(scope='function')
def test_dir(request):
    test_dir = os.path.join(request.config.base_test_dir, request._pyfuncitem.nodeid).replace("::", "_")
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='function')
def api_client(config):
    return ApiClient(config['url'])

@pytest.fixture(scope='function', autouse=True)
def logger(test_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(test_dir, 'test.log')

    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)


