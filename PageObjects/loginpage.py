from Utilities.Utility import Utility

class LoginPage (Utility):
    def __init__(self, driver):
        self.driver = driver
        logger =self.get_logger()
    username = "//input[@name='loginUsername']"
    password = "//input[@name='loginPassword']"
    login_button= "//button[text()='Login']"
    username_errormessage= "//input[@name='loginUsername']//following-sibling::div[contains(text(),'Error message')]"
    password_errormessage ="//input[@name='loginPassword']//following-sibling::div[contains(text(),'Error message')]"

    def enter_username(self,username_text):
        Utility.enter_data(self,self.username,username_text)

    def enter_password(self,password_text):
        Utility.enter_data(self,self.password,password_text)

    def click_login_button(self):
        Utility.buttonclick(self,self.login_button)


