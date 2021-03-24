from .base_page import BasePage
from .locators import ProPageLocators

import time

class ProPage(BasePage):
    def go_to_page(self):
        time.sleep(5)
        pro_button = self.browser.find_element(*ProPageLocators.PRO_BUTTON).click()
        URL = self.browser.current_url

        assert URL == "https://target.my.com/pro"
