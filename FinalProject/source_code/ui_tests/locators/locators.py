from selenium.webdriver.common.by import By


class BasePageLocators:
    BASE_PAGE_LOADED_LOCATOR = ''

    QUERY_LOCATOR = (By.NAME, 'q')
    GO_LOCATOR = (By.ID, 'submit')


class MainPageLocators(BasePageLocators):
    HOME_BUTTON = (By.XPATH, 'fsd')


class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID,'password')
    SUBMIT_BUTTON = (By.ID,'submit')
    NEW_ACCOUNT = (By.XPATH,'//a[@href = "/reg"]')
