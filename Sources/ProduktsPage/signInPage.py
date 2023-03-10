from Sources.ProduktsPage.basePage import BasePage
from selenium.webdriver.common.by import By

class SignInPageLocator():
    signInFieldLocator = (By.ID,"nav-link-accountList")
    loginFieldLocator= (By.ID,"ap_email")
    continueFieldLocator = (By.ID,"continue")
    passwordFieldLocator = (By.ID,"ap_password")
    clickPasswordFieldLocator = (By.ID,"signInSubmit")

class SignInPage(SignInPageLocator,BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_signIn_button(self):
         ButtonElement= self.find_element(*(self.signInFieldLocator))
         ButtonElement.click()

    def fill_login_field(self,login):
        loginPageElement = self.find_element(*(self.loginFieldLocator))
        loginPageElement.clear()
        loginPageElement.send_keys(login)

    def click_to_continue_botton(self):
        loginBottonElement = self.find_element(*(self.continueFieldLocator))
        loginBottonElement.click()

    def fill_password_field(self,password):
        passwoedPageElement = self.find_element(*(self.passwordFieldLocator))
        passwoedPageElement.clear()
        passwoedPageElement.send_keys(password)

    def click_continue_botton(self):
        passwordBottonElement = self.find_element(*(self.clickPasswordFieldLocator))
        passwordBottonElement.click()



