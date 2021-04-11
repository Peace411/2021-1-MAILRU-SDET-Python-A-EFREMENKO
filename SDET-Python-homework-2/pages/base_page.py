import logging
import time

import allure
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 3
BASE_TIMEOUT = 15
logger = logging.getLogger('test')


class BasePage():
    url = "https://target.my.com/"

    def __init__(self, browser, timeout=15):
        self.browser = browser
        logger.info(f'{self.__class__.__name__} page is opening...')
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find(self, how, what, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located((how, what)))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.browser, timeout=timeout)

    def scroll_to(self, element):
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Clicking {what}')
    def click(self, how, what, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {what}. Try {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(how, what, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable((how, what)))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def check_element_is_delete(self, how, what):
        try:
            self.find(how, what, 5)
        except(TimeoutException):
            return True
        else:
            return False

    def check_name_locator(self, locator, name):
        name_locator = (locator[0],
                        locator[1].format(name))
        return name_locator
