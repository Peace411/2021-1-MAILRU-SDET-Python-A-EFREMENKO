import logging

import allure

from mysql_client.builder import MySQLBuilder

from ui_tests.fixtures import *
import pytest

from mysql_client.client import MySqlClient


@pytest.fixture(scope='session')
def mysql_client():
    my_sql_client = MySqlClient(user='test_qa', password='qa_test', db_name='TEST')
    my_sql_client.connect()
    yield my_sql_client
    my_sql_client.connection.close()



def pytest_addoption(parser):
    parser.addoption('--url', default=f'http://{socket.gethostbyname("app")}:8080')
    parser.addoption('--browser', default='chrome')

@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    return {'url': url, 'browser': browser}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

def pytest_configure(config):
    base_test_dir = '/tmp/tests'
    if not hasattr(config, 'workerinput'):  # execute only once on main worker
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

        # save to config for all workers
    config.base_test_dir = base_test_dir
    if not hasattr(config, 'workerinput'):
        my_sql_client = MySqlClient(user='test_qa', password='qa_test', db_name='TEST')
        my_sql_client.recreate_db()
        my_sql_client.connect()
        # Создание таблиц
        my_sql_client.create_table_test_users()
        user = MySQLBuilder(my_sql_client)
        c =user.create_test_user()
        my_sql_client.connection.close()

    @pytest.fixture(scope='function', autouse=True)
    def logger(test_dir, config):
        log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
        log_file = os.path.join(test_dir, 'test.log')

        log_level = logging.INFO

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