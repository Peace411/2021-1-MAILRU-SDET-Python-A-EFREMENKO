from pages.login_page import LoginPage
from pages.param_page import ParamPage
from pages.locators import ParamPageLocators
import pytest
import time

@pytest.mark.parametrize("sel", [ParamPageLocators.AUDIENCES, ParamPageLocators.PRO])
@pytest.mark.ui
def test_param(browser,sel):
    link = "https://target.my.com/"
    page = LoginPage(browser, link)
    page.open()
    page.click_to_login_button()
    page.authorization()
    page = ParamPage(browser, link)
    page.go_to_page(sel)



