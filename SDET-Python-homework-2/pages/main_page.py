from pages.audiencess_page import AudiencesPage
from pages.base_page import BasePage
from pages.company_page import CompanyPage
from pages.locators import MainPageLocator


class MainPage(BasePage):
    def go_to_company(self):
        self.click(*MainPageLocator.CREATE_COMPANY)
        return CompanyPage(self.browser)

    def go_to_audiences(self):
        self.click(*MainPageLocator.AUDIENCES)
        return AudiencesPage(self.browser)
