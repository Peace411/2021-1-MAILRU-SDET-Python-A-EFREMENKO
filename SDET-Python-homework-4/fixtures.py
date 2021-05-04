import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.sources_news_page import SourcesNews
from pages.about_app_page import AboutPage
from pages.setting_page import SettingPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def source_news_page(driver):
    return SourcesNews(driver=driver)


@pytest.fixture
def about_page(driver):
    return AboutPage(driver=driver)


@pytest.fixture
def setting_page(driver):
    return SettingPage(driver=driver)
