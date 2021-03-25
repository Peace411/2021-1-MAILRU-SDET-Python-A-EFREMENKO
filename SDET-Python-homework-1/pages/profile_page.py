from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import EditProfilePageLocators
from selenium.webdriver.common.keys import Keys
import  time

class ProfilePage (BasePage):
    def go_to_profile(self):
        click_on_profile = self.browser.find_element(*EditProfilePageLocators.PROFILE_BUTTON).click()
        URL = self.browser.current_url
        assert URL=="https://target.my.com/profile/contacts",f"{URL} не равен https://target.my.com/profile/contacts"

    def edit_profile(self):
        fio_input = self.browser.find_element(*EditProfilePageLocators.FIO_INPUT)
        fio_input.clear()
        fio_input.send_keys("Ефременко Андрей Андреевич")
        phone_number_input = self.browser.find_element(*EditProfilePageLocators.PHONE_NUMBER)
        phone_number_input.clear()
        phone_number_input.send_keys("+78005553535")
        email_input = self.browser.find_element(*EditProfilePageLocators.INPUT_EMAIL)
        email_input.clear()
        email_input.send_keys("a.efremenko2014@yandex.ru1")
        sumbit_button = self.browser.find_element(*EditProfilePageLocators.SUMBIT_BUTTON).click()
        success_message = self.browser.find_element(*EditProfilePageLocators.SUCCESS_MESSAGE)
        time.sleep(2)
        assert success_message.is_displayed()
