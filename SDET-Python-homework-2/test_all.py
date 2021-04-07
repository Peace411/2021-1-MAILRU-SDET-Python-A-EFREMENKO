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
def test_invalid_password(browser):
    page = LoginPage(browser)
    page.open()
    page.invalid_password_autrization()

@pytest.mark.ui
def test_invalid_login(browser):
    page = LoginPage(browser)
    page.open()
    page.invalid_login_autrization()