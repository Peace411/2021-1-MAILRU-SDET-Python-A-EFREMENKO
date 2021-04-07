import time

import allure
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import AudiencesPageLocators


class AudiencesPage(BasePage):
    @allure.step("""
                           click on the create audience button,
                            set the settings, fill in the name, 
                            save, check the name in the table
                            """
                        )
    def create_audiences(self):
        self.click(*AudiencesPageLocators.CREATE_BUTTON)
        self.click(*AudiencesPageLocators.CHECKBOX)
        self.click(*AudiencesPageLocators.SUBMIT_BUTTON)
        name_input = self.find(*AudiencesPageLocators.NAME_SEGMENT_INPUT)
        name_input.clear()
        name_input.send_keys("test")
        self.click(*AudiencesPageLocators.CREATE_SEGMENT_BUTTON)
        name_in_grid = self.find(*AudiencesPageLocators.NAME_IN_GRID)
        assert name_in_grid.text == "test"

    @allure.step("""
                              check the name in the table,
                              find an item in the table and delete it
                               """
                        )
    def delete_audiences(self):

        name_in_grid = self.find(*AudiencesPageLocators.NAME_IN_GRID)
        assert name_in_grid.text == "test", "такой аудиенции нет "
        self.click(*AudiencesPageLocators.DElETE_AUDIENCE)
        self.click(*AudiencesPageLocators.ACCEPT_BUTTON)
        time.sleep(2)
        assert self.check_element_is_delete(*AudiencesPageLocators.NAME_IN_GRID), "Элемент не удален"
