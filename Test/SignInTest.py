from selenium import webdriver
import unittest
import time
from Sources.signInPage import SignInPage
from Sources.navigtionBar import NavigtionBar
from Sources.produkt import ProduktPage
from Sources.cartPage import DeletProdukt

class MyTest(unittest.TestCase):
      def setUp(self) -> None:
          self.driver = webdriver.Chrome()
          self.driver.implicitly_wait(10)
          self.driver.delete_all_cookies()
          self.driver.maximize_window()
          self.driver.get("https://www.amazon.com/")
          self.SignInPageObj = SignInPage(self.driver)
          self.navigtionBarObj = NavigtionBar(self.driver)
          self.produktObj = ProduktPage(self.driver)
          self.cartPageObj = DeletProdukt(self.driver)




      def test_signInPage (self):
          self.SignInPageObj.click_to_signIn_button()
          self.SignInPageObj.fill_login_field('rafayel1624@gmail.com')
          self.SignInPageObj.click_to_continue_botton()
          time.sleep(3)
          self.SignInPageObj.fill_password_field('2594011624')
          self.SignInPageObj.click_to_password_botton()
          time.sleep(5)
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



