from faker import Faker
from mock.flask_mock import mock_data
from tests.base import BaseCase


class TestMock(BaseCase):
    def test_post_user_mock(self):
        resp = self.client.post_user(name=self.first_name)
        assert '201' in resp[0]
        print(resp)

    def test_post_surname(self):
        resp = self.client.post_surname(name=self.first_name, surname=self.last_name)
        assert self.last_name in resp[-1]
        print(resp)

    def test_put_surname(self):
        fake = Faker()
        surname = fake.last_name()
        mock_data[self.first_name] = self.last_name
        resp = self.client.put_surname(name=self.first_name, surname=surname)
        assert surname in resp[-1]
        print(resp)

    def test_put_no_has_surname(self):
        resp = self.client.put_surname(name=self.first_name, surname=self.last_name)
        assert '400' in resp[0]

    def test_get_user(self):
        mock_data['name'] = self.first_name
        resp = self.client.get_user(name=self.first_name)
        assert self.first_name in resp[-1]
        assert '200' in resp[0]
        print(resp)

    def test_get_invalid_user(self):
        fake = Faker()
        mock_data['name'] = fake.first_name()
        resp = self.client.get_user(name=self.first_name)
        print(resp)
        assert '400' in resp[0]

    def test_delete_surname(self):
        mock_data[self.first_name] = self.last_name
        resp = self.client.delete_surname(name=self.first_name, surname=self.last_name)
        assert '204' in resp[0]
        print(resp)

    def test_delete_surname_non_existing_user(self):
        resp = self.client.delete_surname(name=self.first_name, surname=self.last_name)
        assert '400' in resp[0]
        print(resp)
