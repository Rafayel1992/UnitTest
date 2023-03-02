from selenium.webdriver.common.by import By
from Sources.basePage import  BasePage

class NavigtionBarLocators():
    serchFieldLocators = (By.ID,"twotabsearchtextbox")
    clickSerchBottonLocators = (By.ID, "nav-search-submit-button")
    clickCartBotton = (By.ID,"nav-cart-text-container")
    clickHomePage = (By.ID,"nav-logo-sprites")


class NavigtionBar(NavigtionBarLocators,BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def fill_serch_field(self,txet):
        serchFieldElement =self.find_element(*(self.serchFieldLocators))
        serchFieldElement.clear()
        serchFieldElement.send_keys(txet)

    def click_to_serch_botton(self):
        searchBottomElement = self.find_element(*(self.clickSerchBottonLocators))
        searchBottomElement.click()



    def click_to_cart_botton(self):
        element = self.driver.find_element(*(self.clickCartBotton))
        element.click()

    def go_to_home_page(self):
        element = self.driver.find_element(*(self.clickHomePage))
        element.click()


