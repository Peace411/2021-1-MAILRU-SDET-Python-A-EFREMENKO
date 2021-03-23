from pages.login_page import LoginPage
import pytest
@pytest.mark.ui
def test_logout(browser):
    link = "https://target.my.com/"
    page = LoginPage(browser, link)
    page.open()
    page.click_to_login_button()
    page.authorization()
    page.logout()