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

class MyTestCase(unittest.TestCase):
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
        login_page.do_login('ivantestado@teste.com.br', 'teste123')
        # Verificando se o login ocorreu com sucesso
        time.sleep(0.5)
        assert my_account_page.my_account() == 'Ivan Mendonca'

    @pytest.mark.parametrize('user, passwd, message_error', ler_csv('../../vendors/CSV/test_login.csv'))
    def test_login_error(self, user, passwd, message_error):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)

        # Acessando a tela de login pela HomePage
        time.sleep(0.5)
        home_page.home_signin_enter()
        # Preenchendo com a senha errada
        time.sleep(0.5)
        login_page.do_login(user, passwd)
        time.sleep(0.5)
        assert login_page.message_login() == message_error


if __name__ == '__main__':
    unittest.main()
