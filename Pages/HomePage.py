from selenium.webdriver.common.by import By

from Pages.BasePage import Page

class HomePage(Page):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    login_button_home = (By.CSS_SELECTOR, '.login')

    # Botão que leva para a LoginPage
    def home_signin_enter(self):
        self.do_click(self.login_button_home)
