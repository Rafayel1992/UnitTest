from selenium import webdriver
import unittest
import time
from Sources.ProduktsPage.signInPage import SignInPage
from Sources.Nav_Bar.navigtionBar import NavigtionBar
from Sources.Nav_Bar.produkt import ProduktPage
from Sources.ProduktsPage.cartPage import DeletProdukt

class MyTest(unittest.TestCase):
      def setUp(self) -> None:
          self.driver = webdriver.Chrome()
          self.driver.implicitly_wait(10)
          self.driver.delete_all_cookies()
          self.driver.maximize_window()
          self.driver.get("https://www.amazon.com/")
          self.signInPageObj = SignInPage(self.driver)
          self.navigtionBarObj = NavigtionBar(self.driver)
          self.produktObj = ProduktPage(self.driver)
          self.cartPageObj = DeletProdukt(self.driver)




      def test_signInPage (self):
          self.signInPageObj.click_to_signIn_button()
          self.signInPageObj.fill_login_field('rafayel1624@gmail.com')
          self.signInPageObj.click_to_continue_botton()
          self.signInPageObj.fill_password_field('2594011624')
          time.sleep(5)
          self.signInPageObj.click_continue_botton()
          self.navigtionBarObj.fill_serch_field("toys")
          self.navigtionBarObj.click_to_serch_botton()
          self.produktObj.click_to_produkt()
          self.produktObj.add_to_cart_button()
          self.navigtionBarObj.go_to_home_page()
          self.navigtionBarObj.click_to_cart_botton()
          self.cartPageObj.click_to_delet_botton()
          time.sleep(5)



      def tearDown(self) -> None:
          self.driver.close()



