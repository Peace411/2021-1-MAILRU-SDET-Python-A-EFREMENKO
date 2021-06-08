import logging
import allure
import requests
from ui.locators.locators import MainPageLocators
from ui.pages.base_page import BasePage

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

    @allure.step('go to navbar {name_button}')
    def go_to_navbar_href(self,name_button):
        events_button = (self.locators.EVENTS_BUTTON[0],
                         self.locators.EVENTS_BUTTON[1].format(name_button))
        self.click(events_button)

    @allure.step('go to  overlay link {link}')
    def go_to_overlay_link(self, link):
        overlay_link = (self.locators.OVERLAY_LINK[0],
                        self.locators.OVERLAY_LINK[1].format(link))
        self.click(overlay_link)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[1])
        logger.info(f'{link}  is opening...')
        return self.driver.current_url

    @allure.step('add user in mock and check vk id  on page')
    def check_vk_id(self,name):
        json = {'name':name}
        requests.post(f'http://mock:8083/vk_id/post/user',json=json)
        self.driver.refresh()
        vk_id_on_page =self.find(self.locators.VK_ID)
        assert 'VK ID' in vk_id_on_page.text,'there is no such id'

    def click_logout(self):
        self.click(self.locators.LOGOUT_BUTTON)

    def get_random_text_in_footer(self):
        return self.find(self.locators.RANDOM_TEXT).text
