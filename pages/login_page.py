from pages.base_page import BasePage
from playwright.sync_api import Page
from utilities.read_config import ConfigurationManager


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.current_page = page
        self.USER_NAME = page.locator("//input[@name='username']")
        self.PASSWORD = page.locator("//input[@name='password']")
        self.LOGIN_BUTTON = page.locator("//button[text()='Login']")
        self.ERROR_MSG_LOCATOR = page.locator("//div[@data-component='notification']/div/strong")
        self.BACK_BUTTON = page.locator("//a[text()= ' Zurück zum Login ']")
        self.CONSENT_IFRAME = page.locator("iframe[contains(@src, 'https://plus.demo.net')]")

    def accept_permission_popup(self):
        self.current_page.wait_for_timeout(8_000)
        frame_counter = self.current_page.frames
        for frame in frame_counter:
            accept_button = frame.locator("//button[@id='save-all-pur']")
            if accept_button.is_visible():
                accept_button.click()
        return self.current_page

    def set_username(self, username):
        self.USER_NAME.fill(username)

    def set_password(self, password):
        self.PASSWORD.fill(password)

    def click_login(self):
        self.LOGIN_BUTTON.click()

    def login_to_gmx(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_error_message_locator(self):
        return self.ERROR_MSG_LOCATOR

    def click_back_button(self):
        self.BACK_BUTTON.click()

    def get_back_button_locator(self):
        return self.BACK_BUTTON

    def get_login_button_locator(self):
        return self.LOGIN_BUTTON

