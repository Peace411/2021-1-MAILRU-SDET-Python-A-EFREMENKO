import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def authorization(browser):
    page = LoginPage(browser)
    page.open()
    page.authorization()
    return MainPage