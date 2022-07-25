from selenium.webdriver.common.by import By

class FirstPage(object):
    signIn_homePage = (By.CSS_SELECTOR, '.login')

class AuthenticationPage(object):
    emailBox_login = (By.NAME, 'email')
    passwdBox_login = (By.NAME, 'passwd')
    buttonlogin_login = (By.NAME, 'SubmitLogin')
    message_error = (By.CSS_SELECTOR, ' ol > li')

class MyPage(object):
    client_account = (By.CSS_SELECTOR, '.account')