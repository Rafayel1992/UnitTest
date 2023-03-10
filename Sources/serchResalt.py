from selenium.webdriver.common.by import By

class SerchResaltLocators():
 clickSerchBottonLocators = (By.ID, "nav-search-submit-button")

class SerchResalt(SerchResaltLocators):
    def __init__(self,driver):
        self.driver = driver


def click_to_serch_botton(self):
    searchBottomElement = self.driver.find_element(*(self.clickSerchBottonLocators))
    searchBottomElement.click