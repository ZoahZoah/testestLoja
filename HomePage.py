from BasePage import Page
from Locators import *

class HomePage(Page):
    def __init__(self, driver):
        self.locator = FirstPage
        super(HomePage, self).__init__(driver)

    def home_signin_enter(self):
        self.find_element(*self.locator.signIn_homePage).click()
