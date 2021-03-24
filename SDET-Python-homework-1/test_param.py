from pages.login_page import LoginPage
from pages.audiences_page import AudiencesPage
from pages.pro_page import ProPage
from pages.locators import ProPageLocators
from pages.locators import AudiencesPageLocators
import pytest
import time

@pytest.mark.parametrize("locator,expected_page", [(AudiencesPageLocators.AUDIENCES_BUTTON,AudiencesPage), (ProPageLocators.PRO_BUTTON,ProPage)])
@pytest.mark.ui
def test_param(browser,locator,expected_page):
    link = "https://target.my.com/"
    page = LoginPage(browser, link)
    page.open()
    page.click_to_login_button()
    page.authorization()
    page = expected_page(browser, link)
    page.go_to_page()



