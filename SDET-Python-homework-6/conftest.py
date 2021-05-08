import pytest

from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_top4xx()
        mysql_client.create_top5xx()
        mysql_client.create_top10urls()
        mysql_client.create_method_counts()
        mysql_client.create_number_of_requests()
        mysql_client.connection.close()

