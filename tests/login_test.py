from playwright.sync_api import expect
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login_empty_credentials(self, set_up):
        """
        Verify login with empty credentials.
        """
        expected_error_msg = "Login leider nicht erfolgreich."
        username = " "
        password = " "
        page = set_up
        self.login_page = LoginPage(page)
        self.login_page.accept_permission_popup()
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login()
        expect(self.login_page.get_error_message_locator()).to_have_text(expected_error_msg)

    def test_login_random_credentials(self, set_up):
        """
        Verify login with random credentials.
        """
        expected_error_msg = "Login leider nicht erfolgreich."
        username = "qwertyuiop"
        password = "asdfghjk"
        page = set_up
        self.login_page = LoginPage(page)
        self.login_page.accept_permission_popup()
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login()
        expect(self.login_page.get_error_message_locator()).to_have_text(expected_error_msg)

    def test_login_valid_credentials(self, set_up):
        """
        Verify login with valid credentials.
        """
        expected_error_msg = "Login leider nicht erfolgreich."
        username = " "
        password = " "
        page = set_up
        self.login_page = LoginPage(page)
        self.login_page.accept_permission_popup()
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login()
        expect(self.login_page.get_error_message_locator()).to_have_text(expected_error_msg)

    def test_back_to_login(self, set_up):
        """
        Verify "Zurück zum Login" (back) button.
        """
        username = " "
        password = " "
        page = set_up
        self.login_page = LoginPage(page)
        self.login_page.accept_permission_popup()
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login()
        expect(self.login_page.get_back_button_locator()).to_be_visible()
        self.login_page.click_back_button()
        expect(self.login_page.get_login_button_locator()).to_be_visible()


