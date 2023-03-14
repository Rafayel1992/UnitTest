
from selenium import webdriver
import unittest
from Sources.Nav_Bar.navigtionBar import NavigtionBar
from Sources.Nav_Bar.serchResalts import ProduktPage
from Sources.ProduktsPage.signInPage import SignInPage
import time

class SercheTest (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/")
        self.navigtionBarObj = NavigtionBar(self.driver)
        self.produktObj = ProduktPage(self.driver)
        self.signInPageObj = SignInPage(self.driver)


    def test_sercheResalt(self):
        self.signInPageObj.mouse_move()
        time.sleep(3)
        self.signInPageObj.click_to_signIn_button()
        self.signInPageObj.fill_login_field('rafayel1624@gmail.com')
        self.signInPageObj.click_to_continue_botton()
        time.sleep(5)
        self.signInPageObj.fill_password_field('2594011624')
        self.signInPageObj.click_signIn_botton()
        self.navigtionBarObj.fill_serch_field("toys")
        self.navigtionBarObj.click_to_serch_botton()
        self.produktObj.click_to_serch_produkt()
        self.produktObj.add_to_cart_button()
        time.sleep(3)


    def tearDown(self) -> None:
            self.driver.close()

