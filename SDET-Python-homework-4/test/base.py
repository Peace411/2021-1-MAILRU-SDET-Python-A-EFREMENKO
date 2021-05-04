import pytest
from _pytest.fixtures import FixtureRequest

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.sources_news_page import SourcesNews
from pages.about_app_page import AboutPage
from pages.setting_page import SettingPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.source_news_page: SourcesNews = request.getfixturevalue('source_news_page')
        self.about_page: AboutPage = request.getfixturevalue('about_page')
        self.setting_page: SettingPage = request.getfixturevalue('setting_page')

