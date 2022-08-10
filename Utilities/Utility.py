import inspect
import logging
import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Utility:
    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler('../Reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyPresence(self,locator):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locator)))
        element=self.driver.find_element(By.XPATH,locator)
        if not element.is_displayed():
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'})", element)
        return element

    def enter_data(self,locator,text_tobe_set):
        element= self.verifyPresence(locator)
        if element.text != text_tobe_set:
            element.clear()
            element.send_keys(text_tobe_set)
        assert element.get_attribute("value") == text_tobe_set

    def buttonclick(self,locator):
        element = self.verifyPresence(locator)
        if element.is_displayed():
            element.click()


