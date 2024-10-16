import pytest
from playwright.sync_api import sync_playwright, Playwright
from utilities.read_config import ConfigurationManager


@pytest.fixture
def set_up(playwright: Playwright):
    configuration = ConfigurationManager.get_app_config()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # open new page
    page = context.new_page()
    base_url = configuration["Url"]
    #page.goto("https://www.demo.net/")
    page.goto(base_url)
    yield page
    context.close()
    browser.close()
