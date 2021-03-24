from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".responseHead-module-button-1BMAy4")
    INPUT_EMAIL =(By.CSS_SELECTOR, ".authForm-module-inputWrap-38SKYw> input")
    INPUT_PASSWORD =(By.CSS_SELECTOR, '[type="password"]')
class LogoutPageLocators():
    RIGHT_BUTTON =(By.CSS_SELECTOR, '.right-module-rightWrap-3lL6mf')
    LOGOUT_BUTTON= (By.XPATH,"//a[@href='/logout']")
class EditProfilePageLocators():
    PROFILE_BUTTON= (By.CSS_SELECTOR, '.center-module-profile-BHql9z')
    FIO_INPUT=(By.CSS_SELECTOR, '.js-contacts-field-name .input__wrap>input')
    PHONE_NUBER=(By.CSS_SELECTOR, '.js-contacts-field-phone input')
    INPUT_EMAIL=(By.CSS_SELECTOR, ".js-additional-emails input")
    SUMBIT_BUTTON=(By.CSS_SELECTOR, ".button_submit")
    f= (By.CSS_SELECTOR, ".js-group-form-success-bg")
