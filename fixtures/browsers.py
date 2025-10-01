from pages.authentication.registration_page import RegistrationPage
from playwright.sync_api import Playwright
from _pytest.fixtures import SubRequest
from tools.routes import AppRoute
from config import settings
import pytest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(scope='function', params=settings.browsers)
def page(playwright: Playwright, request: SubRequest):
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)
    

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url()) 
    page = context.new_page()
    
    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill_form(
        settings.test_user.email, 
        settings.test_user.username, 
        settings.test_user.password)
    
    registration_page.click_reg_button()
    
    context.storage_state(path=settings.browser_state_file)
    browser.close()
    
@pytest.fixture(scope='function', params=settings.browsers)
def page_with_state(playwright: Playwright, request: SubRequest, initialize_browser_state):
    yield from initialize_playwright_page(playwright, 
                                          test_name=request.node.name, 
                                          storage_state=settings.browser_state_file, 
                                          browser_type=request.param)
    