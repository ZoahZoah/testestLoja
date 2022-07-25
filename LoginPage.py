from BasePage import Page
from Locators import *

class LoginPage(Page):
    def __init__(self, driver):
        self.locator = AuthenticationPage
        super(LoginPage, self).__init__(driver)

    def enter_email_login(self, user):
        self.find_element(*self.locator.emailBox_login).send_keys(user)

    def enter_passwd_login(self, passwd):
        self.find_element(*self.locator.passwdBox_login).send_keys(passwd)

    def button_to_login(self):
        self.find_element(*self.locator.buttonlogin_login).click()

    def message_error_login(self):
        text = self.find_element(*self.locator.message_error).text
        return text

    def login_login(self, user, passwd):
        self.enter_email_login(user)
        self.enter_passwd_login(passwd)
        self.button_to_login()