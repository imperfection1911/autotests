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


class HeaderLocators:

    CHANGE_PASSWORD_BUTTON = (By.XPATH, '/html/body/div/div/div/header/div[1]/div/div[2]/ul/li[4]/a')


class ChangePageLocators:

    CURRENT_PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/div/div[3]/section/div/div/div/div/div[1]/'
                                        'div/div/div/div[2]/form/div[2]/div[2]/div[2]/input')

    NEW_PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/div/div[3]/section/div/div/div/div/div[1]'
                                    '/div/div/div/div[2]/form/div[3]/div[2]/div[2]/input')

    CONFIRM_PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/div/div[3]/section/div/div/div/div/div[1]'
                                        '/div/div/div/div[2]/form/div[4]/div[2]/div[2]/input')

    CHANGE_PASSWORD_BUTTON = (By.XPATH, '/html/body/div/div/div/div[3]/section/div/div/div/div/div[1]'
                                        '/div/div/div/div[2]/form/div[5]/button')

    CHANGE_PASSWORD_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div')

    CHANGE_PASSWORD_MESSAGE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div[2]/button')

    CHANGE_LOGIN_INPUT = (By.XPATH, '/html/body/div/div/div/div[3]/section/div/div/div/div/div[2]'
                                    '/div/div/div/div[2]/form/div[2]/div[2]/div[2]/input')

    CHANGE_LOGIN_PASSWORD_INPUT = (By.XPATH, '/html/body/div[1]/div/div/div[3]/section/div/div/div/div/div[2]'
                                             '/div/div/div/div[2]/form/div[3]/div[2]/div[2]/input')
    CHANGE_LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div/div/div[3]/section/div/div/div/div/'
                                     'div[2]/div/div/div/div[2]/form/div[4]/button')

    CHANGE_LOGIN_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div')

    CHANGE_LOGIN_MESSAGE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div[2]/button')