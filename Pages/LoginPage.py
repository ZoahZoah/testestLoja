from selenium.webdriver.common.by import By
from Pages.BasePage import *


class LoginPage(Page):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    email = (By.NAME, 'email')
    passwd = (By.NAME, 'passwd')
    submit_login = (By.NAME, 'SubmitLogin')
    message_error = (By.CSS_SELECTOR, ' ol > li')

    # Função que faz login
    def do_login(self, user, passwd):
        self.do_send_keys(self.email, user)
        self.do_send_keys(self.passwd, passwd)
        self.do_click(self.submit_login)

    # Mensagem de erro de login
    def message_login(self):
        element = self.get_element_text(self.message_error)
        return element
