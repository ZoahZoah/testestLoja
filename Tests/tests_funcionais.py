import csv
import time
import pytest
import unittest
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MyAccountPage import MyAccountPage

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo nao encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

class MyTestShop(unittest.TestCase):
    user = 'ivantestado@teste.com.br'
    user_problem = 'ivantestado@teste'
    user_fail_message = 'Invalid email address.'
    passwd = 'teste123'
    passwd_wrong = 'HelloWorld123'
    passwd_fail_message = 'Authentication failed.'

    def setUp(self):
        self.driver = webdriver.Chrome(
            '../vendors/drivers/chromedriver102.exe'
        )
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def test_login(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        # Acessando a tela de login pela HomePage
        time.sleep(0.5)
        home_page.home_signin_enter()
        time.sleep(0.5)
        # Preenchendo os dados de login
        login_page.do_login(self.user, self.passwd)
        # Verificando se o login ocorreu com sucesso
        time.sleep(0.5)
        assert my_account_page.my_account() == 'Ivan Mendonca'

    def test_login_fail(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        # Acessando a tela de login pela HomePage
        time.sleep(0.5)
        home_page.home_signin_enter()
        # Preenchendo com a senha errada
        time.sleep(0.5)
        login_page.do_login(self.user, self.passwd_wrong)
        time.sleep(0.5)
        assert login_page.message_login() == self.passwd_fail_message

    def test_login_fail2(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        # Acessando a tela de login pela HomePage
        time.sleep(0.5)
        home_page.home_signin_enter()
        # Preenchendo com a senha errada
        time.sleep(0.5)
        login_page.do_login(self.user_problem, self.passwd)
        time.sleep(0.5)
        assert login_page.message_login() == self.user_fail_message


if __name__ == '__main__':
    unittest.main()
