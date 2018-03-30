import unittest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.ServicesPage import ServicesPage
from Pages.HeaderPage import Header
from Pages.ChangePasswordAndLoginPage import ChangePasswordAndLoginPage
from Configuration import Configuration
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xmlrunner


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.config = Configuration()
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(command_executor=self.config.read_param('webdriver', 'hub'),
                                       desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get(self.config.read_param('lka', 'url'))

    def test_login(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        login = page.check_login()
        self.assertTrue(login)

    def test_activation_command_repeat(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        page = ServicesPage(self.driver)
        click_result = page.click_command_repeat_button()
        self.assertTrue(click_result)
        repeat_result = page.check_command_repeat_result()
        self.assertTrue(repeat_result)

    def test_change_password(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        current_password = page.password
        page = Header(self.driver)
        page.click_change_password_button()
        page = ChangePasswordAndLoginPage(self.driver)
        new_password = page.generate_password()
        change_password_result = page.fill_change_password_form(current_password, new_password)
        self.assertTrue(change_password_result)
        # меняем пароль обратно
        page.fill_change_password_form(new_password, current_password)

    def test_change_login(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        password = page.password
        page = Header(self.driver)
        page.click_change_password_button()
        page = ChangePasswordAndLoginPage(self.driver)
        current_login = page.get_current_login()
        new_login = 'avzharov'
        change_login_result = page.fill_change_login_form(new_login, password)
        self.assertTrue(change_login_result)
        page.fill_change_login_form(current_login, password)

    def test_cash_transfer(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        page = ServicesPage(self.driver)
        self.assertTrue(page.cash_transfer())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='rep'), failfast=False, buffer=False, catchbreak=False)
