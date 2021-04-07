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


    def invalid_password_autrization(self):
        self.authorization('a.efremenko2014@yandex.ru' , 'fdsfs')
        error_message  = self.find(*LoginPageLocators.EROR_MESSAGE)
        assert error_message.text == "Invalid login or password"

    def invalid_login_autrization(self):
        self.authorization('afdsfsdfsd@yandex.ru','Qwerty12345')
        error_message = self.find(*LoginPageLocators.EROR_MESSAGE)
        assert error_message.text == "Invalid login or password"
