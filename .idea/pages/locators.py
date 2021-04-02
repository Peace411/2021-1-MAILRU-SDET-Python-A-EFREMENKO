from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//*[normalize-space() = 'Войти']")
    INPUT_EMAIL =(By.CSS_SELECTOR, "[name ='email']")
    INPUT_PASSWORD =(By.CSS_SELECTOR, '[type="password"]')
    EROR_MESSAGE = (By.XPATH, "//div [text() = 'Invalid login or password']")

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





class ProPageLocators():
    PRO_BUTTON =(By.XPATH, "//a[contains(@href, 'pro')]")


class MainPageLocator():
    CREATE_COMPANY = (By.XPATH,"//div [string() = 'Создать кампанию']")
    AUDIENCES = (By.XPATH,"//a[contains(@href, '/segments')]")


class CompanyPageLocators():
    NAME_INPUT =(By.CSS_SELECTOR,".js-campaign-name-wrap input")
    BUTTON_MAIL_RU = (By.XPATH,"//div[contains(text(),'Продукты Mail.ru Group')]")
    ADD_LINK = (By.XPATH,"//input[@placeholder='Введите ссылку']")
    INPUT_TITLE = (By.XPATH,"//input[@placeholder='Введите заголовок объявления']")
    INPUT_PHOTO = (By.XPATH,"//input [@accept='.jpg, .jpeg, .png']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR,"[type= 'submit']")
    VIDEO_INPUT = (By.XPATH,"//input [@accept='.mp4']")
    INPUT_TEXT = (By.XPATH,"//textarea[@placeholder ='Введите текст объявления']")
    SAVE_COMPANY = (By.XPATH,"//div/button[string()= 'Создать кампанию']")
    NAME_IN_GRID = (By.XPATH,"//a[text()='test']")
    CHECKBOX = (By.XPATH,"//input [@type='checkbox' ]")
    DROP_BOX = (By.XPATH,"//span[text() = 'Действия' ]")
    DELETE_BUTTOn =(By.XPATH,"//li[text() = 'Удалить' ]")


class AudiencesPageLocators():
    CREATE_BUTTON = (By.XPATH,"//a [contains( @href , '/segments/segments_list/new/') ]")
    CHECKBOX = (By.XPATH,"//input[@type= 'checkbox']")
    SUBMIT_BUTTON =(By.XPATH,"//div[text()  = 'Добавить сегмент']")
    NAME_SEGMENT_INPUT = (By.CSS_SELECTOR,".input_create-segment-form input")
    CREATE_SEGMENT_BUTTON =(By.XPATH,"//button [@class= 'button button_submit']")
    NAME_IN_GRID = (By.XPATH,"//a [string() = 'test']")
    DElETE_AUDIENCE =(By.XPATH , "//div[@class='ReactVirtualized__Grid']//a[text() = 'test']//../..//following-sibling::div//span")
    ACCEPT_BUTTOn = (By.XPATH,"//div [text()= 'Удалить']")
