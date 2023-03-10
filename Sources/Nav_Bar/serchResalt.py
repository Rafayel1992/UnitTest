from selenium.webdriver.common.by import By

class SerchResaltLocator():
 clickSerchBottonLocator = (By.ID, "nav-search-submit-button")

class SerchResalt(SerchResaltLocator):
    def __init__(self,driver):
        self.driver = driver


def click_to_serch_botton(self):
    searchBottomElement = self.driver.find_element(*(self.clickSerchBottonLocator))
    searchBottomElement.click()
