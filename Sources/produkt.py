
from selenium.webdriver.common.by import By
from Sources.basePage import BasePage


class ProduktLocators():
  clickProduktLocators = (By.XPATH,"//img[@class='s-image']")
  addToCartBotton = (By.ID, "add-to-cart-button")

class ProduktPage(ProduktLocators,BasePage):
       def __init__(self, driver):
           super().__init__(driver)
           self.driver = driver



       def click_to_produkt(self):
          clickProduktElement = self.find_element(*(self.clickProduktLocators))
          clickProduktElement.click()


       def add_to_cart_button(self):
         addCartElement = self.find_element(*(self.addToCartBotton))
         addCartElement.click