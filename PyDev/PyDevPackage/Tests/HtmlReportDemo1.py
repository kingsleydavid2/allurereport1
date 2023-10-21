import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PyDevPackage.Pages.LoginPage import LoginPage
from PyDevPackage.Pages.HomePage import HomePage


class Test(unittest.TestCase):


    @classmethod
    def setUpClass(cls)->None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        
        
    def test_login_valid(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/test/newtours/")
        
        driver.implicitly_wait(10)
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin")
        login.click_login()
        
        print("Test completed2")
        
    @unittest.skip("This is . skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
            
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
        
        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Admin/eclipse-workspace/python/PyDev/Reports1'),verbosity=2)

