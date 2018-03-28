from BasePageActions import BasePageActions
import Locators.Locators_lka as Locators
from Configuration import Configuration
import random
import time


class ChangePasswordAndLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.BaseActions = BasePageActions(self.driver)
        self.config = Configuration()

    def fill_change_password_form(self, current_password, new_password):
        try:
            current_password_input = self.BaseActions.find(Locators.ChangePageLocators.CURRENT_PASSWORD_INPUT)
            self.BaseActions.element_input(current_password_input, current_password)
            new_password_input = self.BaseActions.find(Locators.ChangePageLocators.NEW_PASSWORD_INPUT)
            self.BaseActions.element_input(new_password_input, new_password)
            confirm_password_input = self.BaseActions.find(Locators.ChangePageLocators.CONFIRM_PASSWORD_INPUT)
            self.BaseActions.element_input(confirm_password_input, new_password)
            change_password_button = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_PASSWORD_BUTTON)
            time.sleep(3)
            self.BaseActions.click(change_password_button)
            modal_button = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_PASSWORD_MESSAGE_BUTTON)
            self.BaseActions.switch_active()
            message_element = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_PASSWORD_MESSAGE)
            message = self.BaseActions.get_value(message_element)
            self.BaseActions.click(modal_button)
            self.BaseActions.switch_active()
            if message == "Пароль успешно изменен":
                return True
            return False
        except AttributeError:
            self.BaseActions.screenshot('cant_change_password.png')
            return False

    def fill_change_login_form(self, login, password):
        try:
            login_input = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_LOGIN_INPUT)
            self.BaseActions.element_input(login_input, login)
            password_input = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_LOGIN_PASSWORD_INPUT)
            self.BaseActions.element_input(password_input, password)
            button = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_LOGIN_BUTTON)
            time.sleep(3)
            self.BaseActions.click(button)
            modal_button = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_LOGIN_MESSAGE_BUTTON)
            self.BaseActions.switch_active()
            message_element = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_LOGIN_MESSAGE)
            message = self.BaseActions.get_value(message_element)
            self.BaseActions.click(modal_button)
            if "Логин успешно изменен. Новый логин" in message:
                return True
            return False
        except AttributeError:
            self.BaseActions.screenshot('cant_change_login.png')
            return False

    def get_current_login(self):
        login_input = self.BaseActions.find(Locators.ChangePageLocators.CHANGE_LOGIN_INPUT)
        return self.BaseActions.get_attr(login_input, 'value')

    @staticmethod
    def generate_password():
        password = []
        while len(password) < 8:
            password.append(str(random.randint(1,9)))
        return "".join(password)
