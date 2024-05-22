from locators.app_page_locators import AppPageLocators as Locators
from pages.base_page import BasePage


class AppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demo.applitools.com/app.html'

    def load(self):
        self.open(self.url)

    def get_logged_user_name(self):
        return self.find_element(*Locators.LOGGED_USER_NAME)
