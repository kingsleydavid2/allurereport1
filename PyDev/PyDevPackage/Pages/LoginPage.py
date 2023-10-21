from pip._vendor.typing_extensions import Self
class LoginPage():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.username_textbox_name = "userName"
        self.password_textbox_name = "password"
        self.login_button_name = "submit"
        
        
    def enter_username(self,userName):
        self.driver.find_element("name", "userName").clear()
        self.driver.find_element("name", "userName").send_keys(userName)

    def enter_password(self,password):
        self.driver.find_element("name", "password").clear()
        self.driver.find_element("name", "password").send_keys(password)
        
    def click_login(self):
        self.driver.find_element("name", "submit").click()