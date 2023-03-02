
from selenium.webdriver.common.by import By
from Sources.basePage import BasePage
from Sources.navigtionBar import  NavigtionBar

class DeletCartLocators():
    deletBottonLocators =(By.XPATH,"(//input[@value='Delete'])[1]")

class DeletProdukt(DeletCartLocators,BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.navBarObj = NavigtionBar(self.driver)

    def click_to_delet_botton(self):
        element = self.find_element(*(self.deletBottonLocators))
        element.click()


