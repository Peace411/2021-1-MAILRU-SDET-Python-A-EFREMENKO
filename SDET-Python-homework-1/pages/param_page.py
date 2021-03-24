from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ParamPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
import pytest


class ParamPage(BasePage):


    def go_to_page(self,sel):
        time.sleep(5)
        button_on_page = self.browser.find_element(By.CSS_SELECTOR,sel).click()
        if(sel== ParamPageLocators.AUDIENCES):
            URL = self.browser.current_url

            assert URL == "https://target.my.com/segments/segments_list"
        else:
            URL = self.browser.current_url

            assert URL == "https://target.my.com/pro"


