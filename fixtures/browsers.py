from pages.authentication.registration_page import RegistrationPage

from playwright.sync_api import Page, Playwright
import pytest


@pytest.fixture(scope='function')
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    yield browser.new_page()
    browser.close()

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
def chromium_page_with_state(initialize_browser_state: None, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state='./.auth/browser-state.json')
    page = context.new_page()
    yield page
    browser.close()