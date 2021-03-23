from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import time
import pytest

@pytest.mark.ui
def test_login_link(browser):
    link = "https://target.my.com/"
    page = LoginPage(browser, link)
    page.open()
    page.click_to_login_button()
    page.authorization()
    page =ProfilePage(browser, link)
    time.sleep(5)
    page.go_to_profile()
    page.edit_profile()



