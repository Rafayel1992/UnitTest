from selenium.webdriver.common.by import By

class SerchResaltLocator():
  clickSerchBottonLocator = (By.ID, "nav-search-submit-button")
  addToCartBotton = (By.ID, "add-to-cart-button")

class SerchResalt(SerchResaltLocator):
    def __init__(self,driver):
        self.driver = driver


    def click_to_serch_botton(self):
       searchBottomElement = self.driver.find_element(*(self.clickSerchBottonLocator))
       searchBottomElement.click()

    def add_to_cart_button(self):
        addCartElement = self.driver.find_element(*(self.addToCartBotton))
        addCartElement.click()

