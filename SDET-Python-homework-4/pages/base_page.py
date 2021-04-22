import logging
from selenium.webdriver.common.by import By
import allure
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

CLICK_RETRY = 3
BASE_TIMEOUT = 15
logger = logging.getLogger('test')


class BasePage():

    def __init__(self, browser, timeout=15):
        self.browser = browser
        logger.info(f'{self.__class__.__name__} page is opening...')
        self.browser.implicitly_wait(timeout)

    def find(self, how, what, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located((how, what)))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.browser, timeout=timeout)

    def scroll_to(self, element):
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Clicking {what}')
    def click(self, how, what, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {what}. Try {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(how, what, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable((how, what)))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def swipe_up(self, swipetime=200):
        """
        Базовый метод свайпа по вертикали
        Описание работы:
        1. узнаем размер окна телефона
        2. Задаем за X - центр нашего экрана
        3. Указываем координаты откуда и куда делать свайп
        4. TouchAction нажимает на указанные стартовые координаты, немного ждет и передвигает нас из одной точки в другую.
        5. release() наши пальцы с экрана, а perform() выполняет всю эту цепочку команд.
        """
        action = TouchAction(self.browser)
        dimension = self.browser.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    def swipe_to_element(self, locator, max_swipes):
        already_swiped = 0
        while len(self.browser.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe_up()
            already_swiped += 1

    def swipe_element_lo_left(self, how, what):
        """
        :param locator: локатор, который мы ищем
        1. Находим наш элемент на экране
        2. Получаем его координаты (начала, конца по ширине и высоте)
        3. Находим центр элемента (по высоте)
        4. Делаем свайп влево, двигая центр элемента за его правую часть в левую сторону.
        """
        web_element = self.find(how, what, 10)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self.browser)
        action. \
            press(x=right_x, y=middle_y). \
            wait(ms=300). \
            move_to(x=left_x, y=middle_y). \
            release(). \
            perform()
