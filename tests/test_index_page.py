import pytest

from conftest import driver  # TODO: remove me
from pages.app_page import AppPage
from pages.index_page import IndexPage


@pytest.fixture(scope="class")
def index_page(driver):
    index_page = IndexPage(driver)
    index_page.load()
    return index_page


@pytest.fixture(scope="class")
def app_page(driver):
    return AppPage(driver)


class TestIndexPage:

    def test_username_placeholder(self, index_page):
        placeholder = index_page.get_username_input_placeholder()
        print("Placeholder = " + placeholder)
        assert placeholder == 'Enter your username'

    def test_password_placeholder(self, index_page):
        placeholder = index_page.get_password_input_placeholder()
        print("Placeholder = " + placeholder)
        assert placeholder == 'Enter your password'

    def test_login(self, index_page, app_page):
        index_page.log_in('test_user', 'test_password')
        assert app_page.get_logged_user_name().text == 'Jack Gomez'
