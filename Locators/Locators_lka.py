from selenium.webdriver.common.by import By


# Локаторы. Тут хранятся локаторы для элементов страниц, чтобы в случае изменения верстки было легко изменить.
class LoginPageLocators:

    LOGIN_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div[2]/div[2]/section/'
                             'div/div/div/form/div[1]/div[2]/div[2]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div[2]/div[2]/'
                                'section/div/div/div/form/div[2]/div[2]/div[2]/input')
    ENTER_BUTTON = (By.XPATH, '//*[@id="page-wrap"]/div/div[2]/div[2]/section/div/'
                              'div/div/form/div[5]/div/div[1]/button')
    MAIN_PAGE_HEADER = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/div/h1')


class ServicesPageLocators:

    ACTIVATION_COMMAND_REPEAT_BUTTON = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/'
                                                  'div/div[1]/form/div[1]/div[3]/div/button')
    ACTIVATION_COMMAND_REPEAT_RESULT = (By.XPATH,
                                        '//*[@id="page-wrap"]/div/div/div[3]/section/div/'
                                        'div/div/div/div[1]/form/div[1]/div[5]/div/span[1][@style="display: inline;"]')

    PERSONAL_ACCOUNT_TABLE = (By.XPATH, '/html/body/div/div/div/div[3]/section/div/div/div/div/form[2]/div/table/tbody')

    SERVICE_DROP_LIST = (By.XPATH, '//div[@class="select2-result-label"]')

    CASH_TRANSFER_MESSAGE = (By.XPATH, '/html/body/div[4]/div/div/div[1]/div')

    CASH_TRANSFER_MODAL_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[2]/button')

    CASH_TRANSFER_CONTROL_ELEMENT = (By.XPATH, '//button[@class="is-btn is-btn-sm ladda-button blue cntr"]')


class HeaderLocators:

    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//*[@id="page-wrap"]/div/div/header/div[1]/div/div[2]/ul/li[4]/a')


class ChangePageLocators:

    CURRENT_PASSWORD_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/div/div[1]'
                                        '/div/div/div/div[2]/form/div[2]/div[2]/div[2]/input')

    NEW_PASSWORD_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/div'
                                    '/div[1]/div/div/div/div[2]/form/div[3]/div[2]/div[2]/input')

    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/div/div[1]/'
                                        'div/div/div/div[2]/form/div[4]/div[2]/div[2]/input')

    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]'
                                        '/section/div/div/div/div/div[1]/div/div/div/div[2]/form/div[5]/button')

    CHANGE_PASSWORD_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div')

    CHANGE_PASSWORD_MESSAGE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div[2]/button')

    CHANGE_LOGIN_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/div/div[2]'
                                    '/div/div/div/div[2]/form/div[2]/div[2]/div[2]/input')

    CHANGE_LOGIN_PASSWORD_INPUT = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div'
                                             '/div/div/div[2]/div/div/div/div[2]/form/div[3]/div[2]/div[2]/input')
    CHANGE_LOGIN_BUTTON = (By.XPATH, '//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div'
                                     '/div/div[2]/div/div/div/div[2]/form/div[4]/button')

    CHANGE_LOGIN_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div')

    CHANGE_LOGIN_MESSAGE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div[2]/button')
