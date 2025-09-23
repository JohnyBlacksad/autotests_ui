from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_field = page.get_by_test_id('login-form-email-input')
        self.email_label = page.get_by_test_id('login-form-email-input').locator('label')
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        
        self.password_field = page.get_by_test_id('login-form-password-input')
        self.password_label = page.get_by_test_id('login-form-password-input').locator('label')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        
        
        
    def check_visible(self, email: str = None, password: str = None, is_empty: bool = True):
        
        expect(self.email_field).to_be_visible()
        expect(self.email_label).to_have_text('Email')
        
        expect(self.password_field).to_be_visible()
        expect(self.password_label).to_have_text('Password')
        
        if is_empty:
            expect(self.email_input).to_have_value('')
            expect(self.password_input).to_have_value('')
            
        if not is_empty:
            expect(self.email_input).to_have_value(email)
            expect(self.password_input).to_have_value(password)
            
        
    def fill_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        