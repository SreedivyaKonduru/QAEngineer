from Utilities.Utility import Utility
from PageObjects.loginpage import LoginPage
from Data import logindata
import time
import pytest

class Testlogin(Utility):

    logger = Utility.get_logger()

    def test_successfullogin(self,getData):
        try:
            login_page = LoginPage(self.driver)
            login_page.enter_username(getData["username"])
            login_page.enter_password(getData["password"])
            login_page.click_login_button()
            time.sleep(10)
            assert self.driver.current_url == "https://login.dev.qa-experience.com/logged-in"
        except Exception as arg:
            self.logger.error("TestCase Failed")
            raise arg
        else:
            self.logger.info("TestCase Successfully Passed")
        finally:
            self.logger.info("For the user :" +getData["username"])


    @pytest.fixture(params=logindata.LoginData_success)
    def getData(self, request):
        return request.param

