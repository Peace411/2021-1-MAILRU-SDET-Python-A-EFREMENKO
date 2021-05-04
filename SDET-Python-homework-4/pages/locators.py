from selenium.webdriver.common.by import By


class MainPageLocators():
    BUTTON_KEYBOARD = (By.ID, "ru.mail.search.electroscope:id/keyboard")
    INPUT = (By.ID, "ru.mail.search.electroscope:id/input_text")
    NAME_COUNTRY = (By.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_title')
    LIST_COMMANDS = (By.ID, "ru.mail.search.electroscope:id/suggests_list")
    SEND_BUTTON = (By.ID, "ru.mail.search.electroscope:id/text_input_action")
    TEXT_VIEW = (By.XPATH, "//android.widget.TextView[@text= '{}']")
    CARD_TITLE = (By.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_title')
    BURGER_MENU = (By.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')
    NEWS_NAME = (By.ID, 'ru.mail.search.electroscope:id/player_track_name')
    COMMAND_LINE= (By.XPATH,'//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')


class SettingPageLocators():
    SOURCES_NEWS = (By.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    NEWS = (By.XPATH, "//android.widget.TextView[@text= '{}']")
    ABOUT_THE_APP = (By.ID, 'ru.mail.search.electroscope:id/user_settings_about')
    ABOUT_VERSION = (By.ID, 'ru.mail.search.electroscope:id/about_version')
    ABOUT_COPYRIGHT = (By.XPATH, "//*[@resource-id='ru.mail.search.electroscope:id/about_copyright']")
    ITEM_SELECTED =(By.ID,"ru.mail.search.electroscope:id/news_sources_item_selected")
