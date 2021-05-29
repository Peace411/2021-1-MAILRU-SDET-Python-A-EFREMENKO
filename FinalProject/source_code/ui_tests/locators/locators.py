from selenium.webdriver.common.by import By


class BasePageLocators:
    BASE_PAGE_LOADED_LOCATOR = ''

    QUERY_LOCATOR = (By.NAME, 'q')
    GO_LOCATOR = (By.ID, 'submit')


class MainPageLocators(BasePageLocators):
    HOME_BUTTON = (By.XPATH, 'fsd')
    EVENTS_BUTTON = (By.XPATH, "//a[contains(text(), '{}')]")
    EVENTS_LINK_TEMPLATE = (By.XPATH, "//../div//a[contains(text(), '{}')]")
    OVERLAY_LINK = (By.XPATH,"//a[@href = '{}']")
    VK_ID = (By.XPATH,"//li[contains(text(), '{}' )]")
class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'submit')
    NEW_ACCOUNT = (By.XPATH, '//a[@href = "/reg"]')
    FLASH = (By.ID,'flash')


class RegistrationPageLocators(BasePageLocators):
    USER_NAME = (By.ID, 'username')
    EMAIL = (By.ID, 'email')
    PASS = (By.ID, 'password')
    CONFIRM_PASS = (By.ID, 'confirm')
    SDET_CHECK_BOX = (By.ID, 'term')
    SUBMIT_BUTTON = (By.ID, 'submit')
