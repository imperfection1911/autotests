from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from Configuration import Configuration


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
            print(e)

    # ввод данный в элемент
    @staticmethod
    def element_input(element, keys):
        element.clear()
        element.send_keys(keys)

    # клик по элементу
    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def get_value(element):
        return element.text

    def screenshot(self, screenshot_path):
        self.driver.save_screenshot(screenshot_path)


