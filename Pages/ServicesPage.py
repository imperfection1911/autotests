from BasePageActions import BasePageActions
import Locators.Locators_lka as Locators
from Configuration import Configuration
import time


class ServicesPage:

    def __init__(self, driver):
        self.driver = driver
        self.BaseActions = BasePageActions(self.driver)
        self.config = Configuration()

    # клик по кнопке повтора команд
    def click_command_repeat_button(self):
        try:
            button = self.BaseActions.find(Locators.ServicesPageLocators.ACTIVATION_COMMAND_REPEAT_BUTTON)
            self.BaseActions.click(button)
            return True
        except AttributeError:
            self.BaseActions.screenshot('cant_click_repeat_button.png')
            return False

    # проверка повтора команд
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

    # перенос средств
    def cash_transfer(self):
        self.BaseActions.find(Locators.ServicesPageLocators.CASH_TRANSFER_CONTROL_ELEMENT)
        try:
            service_table = self.BaseActions.find(Locators.ServicesPageLocators.PERSONAL_ACCOUNT_TABLE)
            # print(service_table.get_attribute('innerHTML'))
            # проходим по таблице
            rows = service_table.find_elements_by_tag_name('tr')
            for row in rows:
                cells = row.find_elements_by_tag_name('td')
                # print(cells[1].get_attribute('innerHTML'))
                money_cell = cells[1].find_elements_by_tag_name('div')[1]
                money = float(self.BaseActions.get_value(money_cell))
                # ищем сервис с деньгами
                if money > 0:
                    # проверка доступности кнопки
                    button_cell = cells[4].find_element_by_tag_name('button')
                    if button_cell.is_enabled():
                        # вводим 1 рубль в окошко перевода
                        rubles_field = cells[3].find_elements_by_tag_name('input')[0]
                        self.BaseActions.element_input(rubles_field, '1')
                        # выбор сервиса для перевода
                        list_button = cells[2].find_element_by_tag_name('a')
                        self.BaseActions.click(list_button)
                        self.BaseActions.switch_active()
                        service = self.BaseActions.find(Locators.ServicesPageLocators.SERVICE_DROP_LIST)
                        self.BaseActions.click(service)
                        self.BaseActions.switch_active()
                        self.BaseActions.click(button_cell)
                        self.BaseActions.switch_active()
                        message_element = self.BaseActions.find(Locators.ServicesPageLocators.CASH_TRANSFER_MESSAGE)
                        message = self.BaseActions.get_value(message_element)
                        if message == "Средства успешно перенесены":
                            return True
                        self.BaseActions.screenshot('cash_transfer.png')
                        return False
        except AttributeError:
            self.BaseActions.screenshot('cash_transfer.png')
            return False
