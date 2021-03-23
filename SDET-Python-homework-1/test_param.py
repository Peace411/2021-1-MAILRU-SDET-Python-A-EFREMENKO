from selenium.webdriver.common.keys import Keys
from pages.base_locators import LoginPageLocators
import pytest
import time
@pytest.mark.ui
@pytest.mark.parametrize("selector", [".center-module-segments-3y1hDo", ".center-module-billing-x3wyL6"])
def test_param(browser,selector):
    browser.implicitly_wait(15)
    link = "https://target.my.com/"
    browser.get(link)
    login_button = browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
    email_input = browser.find_element(*LoginPageLocators.INPUT_EMAIL)
    email_input.send_keys("a.efremenko2014@yandex.ru")
    password_input = browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
    password_input.send_keys("Qwerty12345")
    password_input.send_keys(Keys.ENTER)
    URL = browser.current_url
    assert URL == "https://target.my.com/dashboard", f"{URL} не равен https://target.my.com/dashboard"
    time.sleep(2)
    button1= browser.find_element_by_css_selector(selector).click()
    if selector==".center-module-segments-3y1hDo":
        time.sleep(3)
        URL = browser.current_url
        assert URL =="https://target.my.com/segments/segments_list"
    else:
        time.sleep(3)
        URL = browser.current_url

        assert URL == "https://target.my.com/billing#deposit"





