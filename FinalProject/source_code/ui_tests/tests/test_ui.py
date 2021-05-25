from base import BaseCase


class TestLoginPage(BaseCase):
    def test_autorization(self):
        self.login_page.user_login('Radmir', 'qwerty12345')
