from BasePageActions import BasePageActions
import Locators.Locators_lka as Locators
from Configuration import Configuration


class ServicesPage:

    def __init__(self, driver):
        self.driver = driver
        self.BaseActions = BasePageActions(self.driver)
        self.config = Configuration()

    def click_command_repeat_button(self):
        try:
            button = self.BaseActions.find(Locators.ServicesPageLocators.ACTIVATION_COMMAND_REPEAT_BUTTON)
            self.BaseActions.click(button)
            return True
        except AttributeError:
            self.BaseActions.screenshot('cant_click_mapping_button.png')
            return False

    def check_command_repeat_result(self):
        try:
            result = self.BaseActions.find(Locators.ServicesPageLocators.ACTIVATION_COMMAND_REPEAT_RESULT)
            result_message = self.BaseActions.get_value(result)
            if result_message == 'Повтор команд активации прошел успешно':
                return True
            return False
        except AttributeError:
            self.BaseActions.screenshot('unsuccessful_command_repeat.png')
            return False
