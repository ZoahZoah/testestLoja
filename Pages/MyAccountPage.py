from selenium.webdriver.common.by import By
from Pages.BasePage import Page

class MyAccountPage(Page):
    def __init__(self, driver):
        super(MyAccountPage, self).__init__(driver)

    client_name = (By.CSS_SELECTOR, '.account span')
    logo_home = (By.CSS_SELECTOR, '.logo')

    # Nome do responsável pela conta
    def my_account(self):
        element = self.get_element_text(self.client_name)
        return element

    # Botão de voltar para a HomePage
    def back_to_homepage(self):
        self.do_click(self.logo_home)
