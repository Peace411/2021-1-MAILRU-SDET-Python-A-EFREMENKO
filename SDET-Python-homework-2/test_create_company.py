import time
import pytest
from  fixtures import  authorization
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.company_page import CompanyPage

@pytest.mark.ui
def test_create_company(browser,authorization):
    page = authorization(browser)
    page.click_on_company()
    page = CompanyPage(browser)
    page.click_on_mail_ru()
    page.create_company()
    page.delete_all_company()
