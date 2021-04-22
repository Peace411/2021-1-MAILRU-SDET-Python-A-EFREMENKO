from pages.base_page import BasePage
from pages.locators import SettingPageLocators


class SourcesNews(BasePage):
    def select_sources_news(self, name_sources_news):
        name_news = (SettingPageLocators.NEWS[0],
                     SettingPageLocators.NEWS[1].format(name_sources_news))
        self.click(*name_news, timeout=20)
        self.find(*SettingPageLocators.ITEM_SELECTED)
        self.browser.back()
        self.browser.back()