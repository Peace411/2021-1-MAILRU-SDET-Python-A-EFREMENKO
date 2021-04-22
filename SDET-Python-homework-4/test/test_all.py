import pytest as pytest

from pages.main_page import MainPage


@pytest.mark.AndroidUI
def test_search_text(browser):
    page = MainPage(browser)
    page.open_keyboard()
    page.text_search(text="Russia")
    page.check_title(expected_text='Россия')
    page.search_command('численность населения россии', '146 млн.')


@pytest.mark.AndroidUI
def test_calculate(browser):
    page = MainPage(browser=browser)
    page.open_keyboard()
    page.text_search(text='2+2')
    page.check_calculate_result(expected_result='4')


@pytest.mark.AndroidUI
def test_radio(browser):
    page = MainPage(browser)
    page = page.go_to_setting()
    page = page.go_to_source_news()
    page.select_sources_news(name_sources_news='Вести FM')
    page = MainPage(browser)
    page.open_keyboard()
    page.text_search(text='News')
    page.check_name_news('Вести ФМ')


@pytest.mark.AndroidUI
def test_check_current_version(browser):
    page = MainPage(browser)
    page = page.go_to_setting()
    page = page.go_to_about_app()
    page.check_current_version()
    page.check_about_copyright()
