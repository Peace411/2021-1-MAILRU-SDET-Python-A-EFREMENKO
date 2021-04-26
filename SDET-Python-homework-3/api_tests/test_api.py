from api_tests.base import ApiBase
import pytest


class TestApi(ApiBase):
    @pytest.mark.API
    def test_valid_login(self, api_client):
        self.api_client.post_login('a.efremenko2014@yandex.ru', 'Qwerty12345')

    @pytest.mark.APi
    def test_create_segment(self, api_client):
        self.api_client.create_segment()

    @pytest.mark.API
    def test_delete_segment(self):
        self.api_client.delete_segment()

    @pytest.mark.API
    def test_create_company(self, api_client):
        self.api_client.create_company()
