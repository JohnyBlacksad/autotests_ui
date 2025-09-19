from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.error_allert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        
    def fill_login_form(self, emai: str, password: str) -> None:
        self.email_input.fill(emai)
        self.password_input.fill(password)
        
        expect(self.email_input).to_have_value(emai)
        expect(self.password_input).to_have_value(password)
        
    def click_login_button(self) -> None:
        self.login_button.click()
        
    def click_registration_link(self) -> None:
        self.registration_link.click()
    
    def check_allert_visible(self):
        expect(self.error_allert).to_be_visible()
        expect(self.error_allert).to_have_text('Wrong email or password')
    