import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=FirefoxOptions()
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
