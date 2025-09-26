from pages.authentication.registration_page import RegistrationPage
from playwright.sync_api import Playwright
from _pytest.fixtures import SubRequest
import pytest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(scope='function')
def chromium_page(playwright: Playwright, request: SubRequest):
    yield from initialize_playwright_page(playwright, test_name=request.node.name)
    

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill_form(email='username@gmail.com', username='username', password='password')
    registration_page.registration_button.click()
    context.storage_state(path='./.auth/browser-state.json')
    
@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state: None, playwright: Playwright, request: SubRequest):
    yield from initialize_playwright_page(playwright, test_name=request.node.name, storage_state='./.auth/browser-state.json')
    