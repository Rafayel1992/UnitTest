
from selenium.webdriver.common.by import By
from Sources.ProduktsPage.basePage import BasePage
from Nav_Bar.navigtionBar import NavigtionBar

class DeletCartLocator():
    deletBottonLocator =(By.XPATH,"(//input[@value='Delete'])[1]")

class DeletProdukt(DeletCartLocator,BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.navBarObj = NavigtionBar(self.driver)

    def click_to_delet_botton(self):
        element = self.find_element(*(self.deletBottonLocator))
        element.click()


