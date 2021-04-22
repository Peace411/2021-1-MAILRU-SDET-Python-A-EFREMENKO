import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.setting_page import SettingPage


class MainPage(BasePage):
    def open_keyboard(self):
        self.click(*MainPageLocators.BUTTON_KEYBOARD)

    def text_search(self, text):
        input1 = self.find(*MainPageLocators.INPUT)
        input1.send_keys(text)
        self.click(*MainPageLocators.SEND_BUTTON)
        self.browser.hide_keyboard()

    def check_title(self, expected_text):
        text = self.find(*MainPageLocators.NAME_COUNTRY)
        assert text.text == expected_text

    def check_calculate_result(self, expected_result):
        locator = (MainPageLocators.TEXT_VIEW[0],
                   MainPageLocators.TEXT_VIEW[1].format(expected_result))
        result = self.find(*locator)
        assert result.text == expected_result

    def check_name_news(self, name_news):
        name_locator = (MainPageLocators.NEWS_NAME[0],
                        MainPageLocators.NEWS_NAME[1].format(name_news))
        name = self.find(*name_locator)
        assert name.text == name_news

    def search_command(self, text_command, expected_text):
        command = (MainPageLocators.TEXT_VIEW[0],
                   MainPageLocators.TEXT_VIEW[1].format(text_command))
        self.click(*command)
        time.sleep(5)
        card_title = self.find(*MainPageLocators.CARD_TITLE)
        assert card_title.text == expected_text

    def go_to_setting(self):
        self.click(*MainPageLocators.BURGER_MENU)
        return SettingPage(browser=self.browser)
