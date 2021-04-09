import os
import time

import allure

from pages.base_page import BasePage
from pages.locators import CompanyPageLocators


def file_path(name):
    repo_root = os.path.abspath(os.path.join(__file__, os.pardir))
    return os.path.join(repo_root, 'files', name)


file1 = file_path("ArcheAge_sample.jpg")
file2 = file_path("Black screen 30 seconds, no sounds, blank for 30 seconds YouTube video, HD.mp4")
name_company = CompanyPageLocators.NAME_COPMANY


class CompanyPage(BasePage):

    def click_on_mail_ru(self):
        mail_button = self.click(*CompanyPageLocators.BUTTON_MAIL_RU)

    @allure.step("""
                             enter a link, enter a name, enter a title, 
                             add a photo, add a video, write a text,
                              create a company, check that the company is created
                              """
                 )
    def create_company(self):
        self.data_entry()
        self.click(*CompanyPageLocators.SAVE_COMPANY)
        time.sleep(5)
        name_in_grid = self.find(*CompanyPageLocators.NAME_IN_GRID)

        assert name_company == name_in_grid.text

    @allure.step("""
                                 click on checkbox,
                                 click on dropbox
                                 click on delete button
                                  """
                 )
    def delete_all_company(self):
        self.click(*CompanyPageLocators.CHECKBOX)
        self.click(*CompanyPageLocators.DROP_BOX)
        self.click(*CompanyPageLocators.DELETE_BUTTON)

    def data_entry(self):
        link = self.find(*CompanyPageLocators.ADD_LINK).send_keys("mail.ru")
        input_name = self.find(*CompanyPageLocators.NAME_INPUT)
        input_name.clear()
        input_name.send_keys(name_company)
        input_title = self.find(*CompanyPageLocators.INPUT_TITLE).send_keys("Загаловок")
        self.find(*CompanyPageLocators.INPUT_PHOTO).send_keys(file1)
        self.click(*CompanyPageLocators.BUTTON_SUBMIT)
        input_video = self.find(*CompanyPageLocators.VIDEO_INPUT).send_keys(file2)
        input_text = self.find(*CompanyPageLocators.INPUT_TEXT).send_keys("Текст")
