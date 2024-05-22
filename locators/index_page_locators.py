from selenium.webdriver.common.by import By


class IndexPageLocators:
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOG_IN_BUTTON = (By.ID, 'log-in')
