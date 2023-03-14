

import time
from selenium import webdriver
import unittest
from Sources.Nav_Bar.serchResalts import ProduktPage
from Sources.ProduktsPage.signInPage import SignInPage
from Sources.ProduktsPage.cartPage import DeletProdukt
from Sources.Nav_Bar.navigtionBar import NavigtionBar



class CartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/")
        self.serchResaltsObj = ProduktPage(self.driver)
        self.signInPageObj = SignInPage(self.driver)
        self.cartPageObj = DeletProdukt(self.driver)
        self.navigtionBarObj = NavigtionBar(self.driver)



    def test_cart(self):
        self.signInPageObj.mouse_move()
        time.sleep(3)
        self.signInPageObj.click_to_signIn_button()
        self.signInPageObj.fill_login_field('rafayel1624@gmail.com')
        self.signInPageObj.click_to_continue_botton()
        time.sleep(5)
        self.signInPageObj.fill_password_field('2594011624')
        self.signInPageObj.click_signIn_botton()
        self.navigtionBarObj.click_to_cart_botton()
        self.cartPageObj.click_to_delet_botton()


        time.sleep(5)




    def tearDown(self) -> None:
            self.driver.close()