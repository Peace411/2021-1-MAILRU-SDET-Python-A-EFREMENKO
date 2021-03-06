import allure

from ui.locators.locators import RegistrationPageLocators
from ui.pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    @allure.step('registration on user name:{name}, pass:{password},email:{email}')
    def registration(self, name, email, password, SDET=True):
        user_name = self.find(self.locators.USER_NAME)
        user_name.send_keys(name)
        email_input = self.find(self.locators.EMAIL)
        email_input.send_keys(email)
        password_input = self.find(self.locators.PASS)
        password_input.send_keys(password)
        confirm = self.find(self.locators.CONFIRM_PASS)
        confirm.send_keys(password)
        if SDET:
            self.click(self.locators.SDET_CHECK_BOX)

        self.click(self.locators.SUBMIT_BUTTON)

    def get_error_message(self):
        message = self.find(self.locators.ERROR_MESSAGE)
        if message.text == '':
            message = self.find(self.locators.ERROR_MESSAGE)
        return message.text

    def find_malevich_square(self):
        main_content = self.find(self.locators.MAIN_CONTENT)
        size_main_content = main_content.size
        self.driver.execute_script("""
        var element = document.querySelector(".uk-width-large");
        element.parentNode.remove(element);
        """, main_content)
        content = self.driver.find_element_by_id("content")

        assert content.size == size_main_content,f'{content.size} != {size_main_content}'
