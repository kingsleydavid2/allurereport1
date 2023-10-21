from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://demo.guru99.com/test/newtours/")

search_box = driver.find_element("name", "userName")

search_box.send_keys('Admin')

search_box1 = driver.find_element("name", "password")

search_box1.send_keys('admin123')

search_box2 = driver.find_element("name", "submit")

search_box2.click()

print("Test is completed")
