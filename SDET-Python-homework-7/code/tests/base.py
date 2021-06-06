import pytest
from faker import Faker

from client import HttpClient

fake = Faker()
class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.client = HttpClient()
        self.first_name=fake.first_name()
        self.last_name = fake.last_name()