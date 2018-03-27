import unittest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.ServicesPage import ServicesPage
from Configuration import Configuration
import xmlrunner


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.config = Configuration()
        self.driver = webdriver.Firefox()
        self.driver.get(self.config.read_param('lka', 'url'))

    def test_login(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        try:
            login = page.check_login()
        except AttributeError:
            login = False
        self.assertTrue(login)

    def test_activation_command_repeat(self):
        page = LoginPage(self.driver)
        page.lka_login(page.login, page.password)
        page = ServicesPage(self.driver)
        click_result = page.click_command_repeat_button()
        self.assertTrue(click_result)
        repeat_result = page.check_command_repeat_result()
        self.assertTrue(repeat_result)

    """def tearDown(self):
        self.driver.close() """

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='rep'), failfast=False, buffer=False, catchbreak=False)
