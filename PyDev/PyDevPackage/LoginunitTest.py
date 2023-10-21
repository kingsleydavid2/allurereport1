from selenium import webdriver
import unittest
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Test(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls)->None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_login_valid(self):
        self.driver.get("https://demo.guru99.com/test/newtours/")
        search_box = self.driver.find_element("name", "userName")
        search_box = search_box.send_keys('Admin')
        search_box1 = self.driver.find_element("name", "password")
        search_box1 = search_box1.send_keys('admin123')
        search_box2 = self.driver.find_element("name", "submit")
        search_box2 = search_box2.click()
        time.sleep(4)
        
    @classmethod
    def tearDownClass(cls)->None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

       



   