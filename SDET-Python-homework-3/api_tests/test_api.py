from api_tests.base import ApiBase


class TestApi(ApiBase):

    def test_valid_login(self, api_client):
        self.api_client.post_login('a.efremenko2014@yandex.ru', 'Qwerty12345')

    def test_create_and_delete_segment(self,api_client):

        self.api_client.create_segment()
        self.api_client.delete_segment()
    def test_create_and_delete_company(self,api_client):
        self.api_client.create_company()
        self.api_client.delete_company()

