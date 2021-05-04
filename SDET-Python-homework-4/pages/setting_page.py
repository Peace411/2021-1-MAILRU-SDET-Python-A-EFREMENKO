import re

from pages.about_app_page import AboutPage
from pages.base_page import BasePage
from pages.locators import SettingPageLocators
import os

from pages.sources_news_page import SourcesNews


class SettingPage(BasePage):

    def go_to_source_news(self):
        self.swipe_to_element(SettingPageLocators.SOURCES_NEWS, 2)
        self.click(*SettingPageLocators.SOURCES_NEWS)
        return SourcesNews(driver=self.driver)

    def go_to_about_app(self):
        self.swipe_to_element(SettingPageLocators.ABOUT_THE_APP, 2)
        self.click(*SettingPageLocators.ABOUT_THE_APP)
        return AboutPage(driver=self.driver)