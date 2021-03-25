from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//*[normalize-space() = 'Войти']")
    INPUT_EMAIL =(By.CSS_SELECTOR, "[name ='email']")
    INPUT_PASSWORD =(By.CSS_SELECTOR, '[type="password"]')


class LogoutPageLocators():
    RIGHT_BUTTON =(By.XPATH, '//div[text()="Баланс: "]')
    LOGOUT_BUTTON= (By.XPATH, "//a[@href='/logout']")


class EditProfilePageLocators():
    PROFILE_BUTTON= (By.XPATH, "//a[contains(@href, '/profile')]")
    FIO_INPUT=(By.CSS_SELECTOR, '.js-contacts-field-name input')
    PHONE_NUMBER=(By.CSS_SELECTOR, '.js-contacts-field-phone input')
    INPUT_EMAIL=(By.CSS_SELECTOR, ".js-additional-emails input")
    SUMBIT_BUTTON=(By.CSS_SELECTOR, ".button_submit")
    SUCCESS_MESSAGE= (By.CSS_SELECTOR, ".js-group-form-success-bg")


class AudiencesPageLocators():
    AUDIENCES_BUTTON = (By.XPATH, "//a[contains(@href, 'segments')]")


class ProPageLocators():
    PRO_BUTTON =(By.XPATH, "//a[contains(@href, 'pro')]")