from .base_page import BasePage
from .base_locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys
from .base_locators import LogoutPageLocators
import  time


class LoginPage (BasePage):
    def click_to_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()

    def authorization(self):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys("a.efremenko2014@yandex.ru")
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys("Qwerty12345")
        password_input.send_keys(Keys.ENTER)
        URL = self.browser.current_url
        assert URL=="https://target.my.com/dashboard",f"{URL} не равен https://target.my.com/dashboard"

    def logout(self):
        time.sleep(3)
        right_button = self.browser.find_element(*LogoutPageLocators.RIGHT_BUTTON).click()
        time.sleep(3)
        logout_button = self.browser.find_element(*LogoutPageLocators.LOGOUT_BUTTON).click()
        URL = self.browser.current_url
        assert URL == "https://target.my.com/", f"{URL} не равен https://target.my.com/"
