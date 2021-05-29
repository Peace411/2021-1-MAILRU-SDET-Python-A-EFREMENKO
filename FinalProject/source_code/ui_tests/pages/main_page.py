import logging
import time

# from mock.flask_mock import MOCK_DATA
import allure
import requests

from ui_tests.locators.locators import MainPageLocators
from ui_tests.pages.base_page import BasePage

logger = logging.getLogger('test')


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step('go to link {event_button}{event}')
    def go_to_navbar_link(self, event_button, event):
        logger.info(f'{event_button + event} link is opening...')
        events_button = (self.locators.EVENTS_BUTTON[0],
                         self.locators.EVENTS_BUTTON[1].format(event_button))
        events_button = self.find(events_button)
        self.action_chains.move_to_element(events_button).perform()
        event_locator = (self.locators.EVENTS_LINK_TEMPLATE[0],
                         self.locators.EVENTS_LINK_TEMPLATE[1].format(event))
        self.click(event_locator)


    @allure.step('go to  overlay link {link}')
    def go_to_overlay_link(self, link):
        overlay_link = (self.locators.OVERLAY_LINK[0],
                        self.locators.OVERLAY_LINK[1].format(link))
        self.click(overlay_link)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[1])
        logger.info(f'{link}  is opening...')
        return self.driver.current_url
    def check_vk_id(self,name):
        vk_id = requests.get(f'http://mock:8083/vk_id/{name}')
        vk_id = vk_id.json()
        vk_id_element = (self.locators.VK_ID[0],
                        self.locators.VK_ID[1].format(vk_id))
        vk_id_on_page =self.find(vk_id_element)
        assert  vk_id_on_page == vk_id

