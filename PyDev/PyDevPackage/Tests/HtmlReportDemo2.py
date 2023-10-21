import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestStringMethods(unittest.TestCase):

    @classmethod
    def test_setUpClass(cls)->None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        
        
    def test_search_1(self):
        driver = self.driver
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.driver.implicitly_wait(10)
        self.driver.find_element("name", "userName").clear()
        self.driver.find_element("name", "userName").send_keys("Admin")
        self.driver.find_element("name", "password").clear()
        self.driver.find_element("name", "password").send_keys("admin")
        self.driver.find_element("name", "submit").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x, "Login: Mercury Tours")
        self.driver.quit()
      
    
   
        
    print("Test completed2")
        
            
    if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Admin/eclipse-workspace/python/PyDev/Reports1'))
      