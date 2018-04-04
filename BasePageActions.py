from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from Configuration import Configuration
from selenium.webdriver.common.action_chains import ActionChains


# Тут описываются стандартные действия, которые могут проводится со страницей
class BasePageActions:

    def __init__(self, driver):
        self.driver = driver
        self.config = Configuration()

    # поиск элемента
    def find(self, locator):
        try:
            element = WebDriverWait(self.driver, int(self.config.read_param('webdriver', 'wait_timeout'))).\
                until(EC.presence_of_element_located(locator))
            return element
        except selenium.common.exceptions.TimeoutException as e:
            return False

    def wait_for_visibility(self, element):
        try:
            visible_element = WebDriverWait(self.driver, int(self.config.read_param('webdriver', 'wait_timeout'))).\
                until(EC.visibility_of(element))
            return visible_element
        except selenium.common.exceptions.TimeoutException as e:
            return False

    def clickable(self, element):
        try:
            clickable_element = WebDriverWait(self.driver, int(self.config.read_param('webdriver', 'wait_timeout')))\
                .until(EC.element_to_be_clickable(element))
            return clickable_element
        except selenium.common.exceptions.TimeoutException as e:
            return False

    # ввод данных в элемент
    @staticmethod
    def element_input(element, keys):
        element.clear()
        element.send_keys(keys)

    # клик по элементу
    @staticmethod
    def click(element):
        element.click()

    # получить значение элемента
    @staticmethod
    def get_value(element):
        return element.text

    # получить значение атрибута
    @staticmethod
    def get_attr(element, attributte):
        return element.get_attribute(attributte)

    # сделать скриншот
    def screenshot(self, screenshot_path):
        self.driver.save_screenshot(screenshot_path)

    # кликнуть алерт
    def accept_alert(self):
        try:
            WebDriverWait(self.driver, int(self.config.read_param('webdriver', 'wait_timeout')))\
                .until(EC.alert_is_present())
        except selenium.common.exceptions.TimeoutException as e:
            print(e)
        alert = self.driver.switch_to.alert
        alert.accept()

    # Перевести курсор и кликнуть
    def move_mouse_cursor_and_click(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    # переключится на модальное окно
    def switch_active(self):
        self.driver.switch_to.active_element
