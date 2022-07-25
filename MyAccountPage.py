from BasePage import Page
from Locators import *

class MyAccountPage(Page):
    def __init__(self, driver):
        self.locator = MyPage
        super(MyAccountPage, self).__init__(driver)

    def my_account(self):
        text = self.find_element(*self.locator.client_account).text
        return text
