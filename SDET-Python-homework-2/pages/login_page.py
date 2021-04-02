import pytest

from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage (BasePage):
    url = "https://target.my.com/"
    def authorization(self):
        login_button = self.click(*LoginPageLocators.LOGIN_LINK)
        email_input = self.find(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys("a.efremenko2014@yandex.ru")
        password_input = self.find(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys("Qwerty12345")
        password_input.send_keys(Keys.ENTER)
        self.browser.set_page_load_timeout(15)
        URL = self.browser.current_url
        assert URL=="https://target.my.com/dashboard",f"{URL} не равен https://target.my.com/dashboard"

    def novalid_password_autrization(self):
        login_button = self.click(*LoginPageLocators.LOGIN_LINK)
        email_input = self.find(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys("a.efremenko2014@yandex.ru")
        password_input = self.find(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys("fdsfdsf")
        password_input.send_keys(Keys.ENTER)
        error_message  = self.find(*LoginPageLocators.EROR_MESSAGE)
        assert error_message.text == "Invalid login or password"

    def novalid_login_autrization(self):
        login_button = self.click(*LoginPageLocators.LOGIN_LINK)
        email_input = self.find(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys("aEfremenko2014@yandex.ru")
        password_input = self.find(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys("Qwerty12345")
        password_input.send_keys(Keys.ENTER)
        error_message  = self.find(*LoginPageLocators.EROR_MESSAGE)
        assert error_message.text == "Invalid login or password"
