import pytest

from pages.login_page import LoginPage

@pytest.mark.ui
def test_no_valid_password(browser):
    page = LoginPage(browser)
    page.open()
    page.novalid_login_autrization()