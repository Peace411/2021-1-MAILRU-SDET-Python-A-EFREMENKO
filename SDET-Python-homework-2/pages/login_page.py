import pytest
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys
user = "a.efremenko2014@yandex.ru"
password = "Qwerty12345"

class LoginPage (BasePage):
    url = "https://target.my.com/"
    def authorization(self,user=user,password=password):
        self.click(*LoginPageLocators.LOGIN_LINK)
        email_input = self.find(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(user)
        password_input = self.find(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)


    def invalid_autrization(self,invalid_email,invalid_password):
        self.authorization(invalid_email , invalid_password)
        error_message  = self.find(*LoginPageLocators.EROR_MESSAGE)
        assert error_message.text == "Invalid login or password"


