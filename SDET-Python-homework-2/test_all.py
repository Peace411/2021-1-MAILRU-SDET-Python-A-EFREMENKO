import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
def test_create_company(authorization):
    page = authorization.go_to_company()
    page.click_on_mail_ru()
    page.create_company()
    page.delete_all_company()

@pytest.mark.ui
def test_create_audiences(authorization):
    page = authorization.go_to_audiences()
    page.create_audiences()
    page.delete_audiences()

@pytest.mark.ui
@pytest.mark.parametrize('email,password', [('a.efremenko2014@yandex.ru', '123'), ('a232@yandex.ru', 'Qwerty12345')])
def test_invalid_credentials(browser, email, password):
    page = LoginPage(browser)
    page.open()
    page.invalid_autrization(email, password)

