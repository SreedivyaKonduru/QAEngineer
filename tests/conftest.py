
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver= None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service("C:\\Divya\\SelDrivers\\geckodriver.exe"))
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://login.dev.qa-experience.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
