
from selenium import webdriver
import unittest
import time
from Sources.Nav_Bar.navigtionBar import NavigtionBar
from Sources.Nav_Bar.produkt import ProduktPage

class SercheTest (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/")
        self.navigtionBarObj = NavigtionBar(self.driver)
        self.produktObj = ProduktPage(self.driver)

         
    def test_sercheResalt(self):
        self.navigtionBarObj.fill_serch_field("toys")
        self.navigtionBarObj.click_to_serch_botton()
        self.produktObj.click_to_produkt()
        self.produktObj.add_to_cart_button()

    def tearDown(self) -> None:
            self.driver.close()

