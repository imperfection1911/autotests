from selenium.webdriver.common.by import By


# Локаторы. Тут хранятся локаторы для элементов страниц, чтобы в случае изменения верстки было легко изменить.
class LoginPageLocators:

    LOGIN_INPUT = (By.XPATH, '//input[@class="input-field" and @placeholder="ID или номер Абонентского договора"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@class="input-field" and @placeholder="Пароль для входа"]')
    ENTER_BUTTON = (By.XPATH, '//button[@class="is-btn ladda-button is-btn-1_3"]')
    MAIN_PAGE_HEADER = (By.XPATH, '//div[@class="is-content is-styles"]/h1')


class ServicesPageLocators:

    ACTIVATION_COMMAND_REPEAT_BUTTON = (By.XPATH, '//button[@class="is-btn ladda-button red"]')
    ACTIVATION_COMMAND_REPEAT_RESULT = (By.XPATH,
                                        '//span[@class="repeat-command-success" and @style="display: inline;"]')
