from ui_tests.locators.locators import LoginPageLocators
from  ui_tests.pages.base_page import BasePage
class LoginPage(BasePage):

    locators = LoginPageLocators()
    def user_login(self,name,password):
        login_input =self.find(self.locators.LOGIN_INPUT)
        login_input.send_keys(name)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.click(self.locators.SUBMIT_BUTTON)
