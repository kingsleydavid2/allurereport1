from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://google.com")

search_box = driver.find_element("name", "q")

search_box.send_keys('ChromeDriver')

search_box.submit()

