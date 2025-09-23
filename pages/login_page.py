from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form = LoginFormComponent(page)
       
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.error_allert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        
    def click_login_button(self) -> None:
        self.login_button.click()
        
    def click_registration_link(self) -> None:
        self.registration_link.click()
    
    def check_allert_visible(self):
        expect(self.error_allert).to_be_visible()
        expect(self.error_allert).to_have_text('Wrong email or password')
    