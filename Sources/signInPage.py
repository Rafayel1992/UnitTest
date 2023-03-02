from Sources.basePage import BasePage
from selenium.webdriver.common.by import By

class SignInPageLocators():
    signInFieldLocators = (By.ID,"nav-link-accountList")
    loginFieldLocators = (By.ID,"ap_email")
    continueFieldLocators = (By.ID,"continue")
    passwordFieldLocators = (By.ID,"ap_password")
    clickPasswordFieldLocators = (By.ID,"signInSubmit")

class SignInPage(SignInPageLocators,BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_signIn_button(self):
         ButtonElement= self.find_element(*(self.signInFieldLocators))
         ButtonElement.click()

    def fill_login_field(self,login):
        loginPageElement = self.find_element(*(self.loginFieldLocators))
        loginPageElement.clear()
        loginPageElement.send_keys(login)

    def click_to_continue_botton(self):
        loginBottonElement = self.find_element(*(self.continueFieldLocators))
        loginBottonElement.click()

    def fill_password_field(self,password):
        passwoedPageElement = self.find_element(*(self.passwordFieldLocators))
        passwoedPageElement.clear()
        passwoedPageElement.send_keys(password)

    def click_to_password_botton(self):
        passwordBottonElement = self.find_element(*(self.clickPasswordFieldLocators))
        passwordBottonElement.click()



