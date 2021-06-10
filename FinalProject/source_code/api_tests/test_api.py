import pytest

from api_client.client import ResponseStatusCodeException
from base import BaseCaseApi


@pytest.mark.api
class TestMyAppCaseApi(BaseCaseApi):

    def test_add_user(self):
        self.new_user = self.api_user_builder.create_user()
        self.add_user(self.new_user.username, self.new_user.password, self.new_user.email)
        user = self.mysql_client.get_user(username=self.new_user.username,
                                          password=self.new_user.password,
                                          email=self.new_user.email)
        assert user.username == self.new_user.username and user.password == self.new_user.password \
               and user.email == self.new_user.email

    def test_delete_user(self):
        new_database_user = self.mysql_builder.create_test_user()
        resp =self.client_api.get_delete_user(username=new_database_user.username)
        assert self.mysql_client.check_exist_user(id=new_database_user.id) is False


    def test_block_user(self):  # Test block user
        new_database_user = self.mysql_builder.create_test_user()
        self.client_api.post_login(new_database_user.username , new_database_user.password )
        self.client_api.get_block_user(username=new_database_user.username)
        changed_user = self.mysql_client.get_user(id=new_database_user.id)
        assert changed_user.access == 0
        assert  changed_user.active == 0
    def test_unblock_user(self):
        new_database_user = self.mysql_builder.create_test_user(access=0)
        self.client_api.get_unblock_user(username=new_database_user.username)
        changed_user = self.mysql_client.get_user(id=new_database_user.id)
        assert changed_user.access == 1


    def test_status(self):
        self.client_api.get_status()

    def test_registration(self):
        new_user = self.api_user_builder.create_user()
        response = self.client_api.post_registration(username=new_user.username,
                                                     password=new_user.password,
                                                     email=new_user.email,
                                                     confirm=new_user.password)
        assert 'welcome' in response.headers['Location']

    def test_no_sdet_registration(self):
        new_user = self.api_user_builder.create_user()
        response = self.client_api.post_registration(username=new_user.username,
                                                     password=new_user.password,
                                                     email=new_user.email,
                                                     confirm=new_user.password,
                                                     term='',
                                                     expected_status=400

                                                     )
        assert 'reg' in response.headers['Location']

    def test_logout(self):
        response = self.client_api.get_logout()
        assert 'login' in response.headers['Location']
        user = self.mysql_client.get_user(username=self.main_user.username)
        assert user.active == 0

    def test_check_findjs(self):
        self.client_api.get_find_me(expected_status=200)

    def test_negative_username_registration(self):
        user = self.api_user_builder.create_user(username='1234')
        with pytest.raises(ResponseStatusCodeException):
            self.client_api.post_registration(username=user.username, password=user.password,
                                              email=user.email, confirm=user.password)


    def test_negative_password_registration(self):
        user = self.api_user_builder.create_user(password='')
        with pytest.raises(ResponseStatusCodeException):
            self.client_api.post_registration(username=user.username, password=user.password,
                                              email=user.email, confirm=user.password)


    def test_negative_confirm_registration(self):
        user = self.api_user_builder.create_user()
        with pytest.raises(ResponseStatusCodeException):
            self.client_api.post_registration(username=user.username, password=user.password,
                                              email=user.email, confirm='')


    def test_negative_term_registration(self):  # 2 Bug with term
        user = self.api_user_builder.create_user()
        with pytest.raises(ResponseStatusCodeException):
            self.client_api.post_registration(username=user.username, password=user.password,
                                              email=user.email, confirm=user.password, term='n')

    def test_negative_login(self):
        user = self.api_user_builder.create_user()
        with pytest.raises(ResponseStatusCodeException):
            self.client_api.post_login(username=user.username, password=user.password)
