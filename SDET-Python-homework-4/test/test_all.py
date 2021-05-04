import pytest as pytest
from pages.main_page import MainPage
from base import BaseCase


class Test(BaseCase):
    @pytest.mark.AndroidUI
    def test_search_text(self):
        self.main_page.open_keyboard()
        self.main_page.text_search(text="Russia")
        self.main_page.check_title(expected_text='Россия')
        self.main_page.search_command('численность населения россии', '146 млн.')

    @pytest.mark.AndroidUI
    def test_calculate(self):
        self.main_page.open_keyboard()
        self.main_page.text_search(text='2+2')
        self.main_page.check_calculate_result(expected_result='4')

    @pytest.mark.AndroidUI
    def test_radio(self):

        self.main_page.go_to_setting()
        self.setting_page.go_to_source_news()
        self.source_news_page.select_sources_news(name_sources_news='Вести FM')
        self.main_page.open_keyboard()
        self.main_page.text_search(text='News')
        self.main_page.check_name_news('Вести ФМ')

    @pytest.mark.AndroidUI
    def test_check_current_version(self):
        self.main_page.go_to_setting()
        self.setting_page.go_to_about_app()
        self.about_page.check_current_version()
        self.about_page.check_about_copyright()
