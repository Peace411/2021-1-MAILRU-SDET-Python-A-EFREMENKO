from .locators import AudiencesPageLocators
from .base_page import BasePage
import time

class AudiencesPage(BasePage):
    def go_to_page(self):
        time.sleep(5)
        button_audiences = self.browser.find_element(*AudiencesPageLocators.AUDIENCES_BUTTON).click()
        URL = self.browser.current_url
        assert URL== "https://target.my.com/segments/segments_list"

