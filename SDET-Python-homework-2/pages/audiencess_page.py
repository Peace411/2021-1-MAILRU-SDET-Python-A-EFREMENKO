import time

import allure

from pages.base_page import BasePage
from pages.locators import AudiencesPageLocators


class AudiencesPage(BasePage):
    @allure.step("""
                           click on the create audience button,
                            set the settings, fill in the name, 
                            save, check the name in the table
                            """
                 )
    def create_audiences(self, name):
        self.click(*AudiencesPageLocators.CREATE_BUTTON)
        self.click(*AudiencesPageLocators.CHECKBOX)
        self.click(*AudiencesPageLocators.SUBMIT_BUTTON)
        name_input = self.find(*AudiencesPageLocators.NAME_SEGMENT_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        self.click(*AudiencesPageLocators.CREATE_SEGMENT_BUTTON)
        name_locator = self.check_name_locator(AudiencesPageLocators.NAME_IN_GRID, name)
        name_in_grid = self.find(*name_locator)
        assert name_in_grid.text == name

    @allure.step("""
                              check the name in the table,
                              find an item in the table and delete it
                               """
                 )
    def delete_audiences(self, name):
        name_locator = self.check_name_locator(AudiencesPageLocators.NAME_IN_GRID, name)
        name_in_grid = self.find(*name_locator)
        assert name_in_grid.text == name, "такой аудиенции нет "
        delete_locator = self.check_name_locator(AudiencesPageLocators.DElETE_AUDIENCE, name)
        self.click(*delete_locator)
        self.click(*AudiencesPageLocators.ACCEPT_BUTTON)
        time.sleep(2)
        assert self.check_element_is_delete(*name_locator), "Элемент не удален"
