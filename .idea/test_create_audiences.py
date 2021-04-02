import time

import pytest

from pages.audiencess_page import AudiencesPage
from  fixtures import  authorization

@pytest.mark.ui
def test_create_audiences(browser,authorization):
    page = authorization(browser)
    page.go_to_audiences()
    page = AudiencesPage(browser)
    page.create_audiences()
    page.delete_audiences()
