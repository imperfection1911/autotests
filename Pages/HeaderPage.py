from BasePageActions import BasePageActions
import Locators.Locators_lka as Locators
from Configuration import Configuration


class Header:

    def __init__(self, driver):
        self.driver = driver
        self.BaseActions = BasePageActions(self.driver)
        self.config = Configuration()

    def click_change_password_button(self):
        try:
            button = self.BaseActions.find(Locators.HeaderLocators.CHANGE_PASSWORD_BUTTON)
            self.BaseActions.move_mouse_cursor_and_click(button)
            return True
        except AttributeError:
            self.BaseActions.screenshot('cant_click_change_password_button.png')
            return False
