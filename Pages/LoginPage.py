from BasePageActions import BasePageActions
import Locators.Locators_lka as Locators
from Configuration import Configuration


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.BaseActions = BasePageActions(self.driver)
        self.config = Configuration()
        self.login = self.config.read_param('lka', 'login')
        self.password = self.config.read_param('lka', 'password')

    def lka_login(self, login, password):
        login_input = self.BaseActions.find(Locators.LoginPageLocators.LOGIN_INPUT)
        self.BaseActions.element_input(login_input, login)
        password_input = self.BaseActions.find(Locators.LoginPageLocators.PASSWORD_INPUT)
        self.BaseActions.element_input(password_input, password)
        enter_button = self.BaseActions.find(Locators.LoginPageLocators.ENTER_BUTTON)
        self.BaseActions.click(enter_button)

    def check_login(self):
        main_page_header = self.BaseActions.find(Locators.LoginPageLocators.MAIN_PAGE_HEADER)
        if self.BaseActions.get_value(main_page_header) == "Мои услуги":
            return True
        return False



