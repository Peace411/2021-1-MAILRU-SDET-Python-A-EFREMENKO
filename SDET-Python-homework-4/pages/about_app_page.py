import re

from pages.base_page import BasePage
from pages.locators import SettingPageLocators
import os


class AboutPage(BasePage):
    def check_current_version(self):
        version_in_app = self.find(*SettingPageLocators.ABOUT_VERSION).text
        file = os.path.basename(os.path.join(os.path.dirname(__file__),
                                             'stuff/Marussia_v1.39.1.apk'))

        version = re.search(r'\d.\d\d.\d', file)
        assert 'Версия ' + version[0] == version_in_app

    def check_about_copyright(self):
        about_copy = self.find(*SettingPageLocators.ABOUT_COPYRIGHT).text
        assert about_copy == 'Mail.ru Group © 1998–2021. Все права защищены.'