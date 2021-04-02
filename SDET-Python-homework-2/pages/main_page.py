from pages.base_page import BasePage
from pages.locators import MainPageLocator


class MainPage(BasePage):
    def click_on_company(self):
        buttton_company = self.click(*MainPageLocator.CREATE_COMPANY)

    def go_to_audiences(self):
        self.click(*MainPageLocator.AUDIENCES)
