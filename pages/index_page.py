from locators.index_page_locators import IndexPageLocators as Locators
from pages.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demo.applitools.com/'

    def load(self):
        self.open(self.url)

    def get_username_input(self):
        return self.find_element(*Locators.USERNAME_INPUT)

    def get_password_input(self):
        return self.find_element(*Locators.PASSWORD_INPUT)

    def get_log_in_button(self):
        return self.find_element(*Locators.LOG_IN_BUTTON)

    def get_username_input_placeholder(self):
        return self.find_element(*Locators.USERNAME_INPUT).get_attribute('placeholder')

    def get_password_input_placeholder(self):
        return self.find_element(*Locators.PASSWORD_INPUT).get_attribute('placeholder')

    def log_in(self, username, password):
        username_input = self.get_username_input()
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.get_password_input()
        password_input.clear()
        password_input.send_keys(password)

        self.get_log_in_button().click()
