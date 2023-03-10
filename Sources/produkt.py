
from selenium.webdriver.common.by import By
from Sources.basePage import BasePage


class ProduktLocator():
  clickProduktLocators = (By.XPATH,"//img[@class='s-image']")
  addToCartBotton = (By.ID, "add-to-cart-button")

class ProduktPage(ProduktLocator,BasePage):
       def __init__(self, driver):
           super().__init__(driver)
           self.driver = driver



       def click_to_produkt(self):
          clickProduktElement = self.find_element(*(self.clickProduktLocator))
          clickProduktElement.click()


       def add_to_cart_button(self):
         addCartElement = self.find_element(*(self.addToCartBotton))
         addCartElement.click()
