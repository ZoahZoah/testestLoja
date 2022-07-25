import time
import unittest
from selenium import webdriver
from HomePage import HomePage
from LoginPage import LoginPage
from MyAccountPage import MyAccountPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            'vendors/drivers/chromedriver102.exe'
        )
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_login(self):
        print('\n' + str('Teste(1) - Validação de login'))
        time.sleep(0.5)
        # Acessando a tela de login pela HomePage
        home_page = HomePage(self.driver)
        home_page.home_signin_enter()
        login_page = LoginPage(self.driver)
        time.sleep(0.5)
        # Preenchendo os dados de login
        login_page.login_login('ivantestado@teste.com.br', 'teste123')
        time.sleep(0.5)
        # Verificando se o login ocorreu com sucesso
        my_account_page = MyAccountPage(self.driver)
        assert my_account_page.my_account() == 'Ivan Mendonca'
        print('\n' + str('Teste 1 foi um sucesso'))

    def test_login_error1(self):
        print("\n" + str('Teste(2) - Validação de erro com login e senha errado'))
        time.sleep(0.5)
        # Acessando a tela de login pela HomePage
        home_page = HomePage(self.driver)
        home_page.home_signin_enter()
        login_page = LoginPage(self.driver)
        time.sleep(0.5)
        # Preenchendo com a senha errada
        login_page.login_login('ivantestado@teste.com.br', 'teste321')
        time.sleep(0.5)
        assert login_page.message_error_login() == 'Authentication failed.'
        # Preenchendo com o e-mail errado
        if login_page.message_error_login() == 'Authentication failed.':
            login_page.login_login('ivantestado@balacobaco.com.br', 'teste123')
            time.sleep(0.5)
            assert login_page.message_error_login() == 'Invalid email address.'


if __name__ == '__main__':
    unittest.main()
