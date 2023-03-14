from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import  mouse


class mouseMoveLocator():
    moseMoveLocator = (By.ID,'nav-link-accountList')



class BasePage(mouseMoveLocator):
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,by:By, value: str):
        try:
               elemnt = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((by,value)))
        except:
            print(f"Error 1 : Elemnt ({by}, {value})not visible")
        return elemnt


    def mouse_move(self):

        action = ActionChains(self.driver)

        #action.move_to_element(self.find_element(*(self.moseMoveLocator))).perform()
       # action.perform()









    def get_title(self):
        return self.driver.title
    
    
