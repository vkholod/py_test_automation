from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def find_elements(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(locator))

    def open(self, url):
        self.driver.get(url)
