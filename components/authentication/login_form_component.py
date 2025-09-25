from components.base_component import BaseComponent
from elements.input import Input
from elements.label import Label
from playwright.sync_api import Page
import allure

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.email_label = Label(page, 'login-form-email-input', 'Email placeholder')
        self.email_input = Input(page, 'login-form-email-input', 'Email field')
        
        self.password_label = Label(page, 'login-form-password-input', 'Password placeholder')
        self.password_input = Input(page, 'login-form-password-input', 'Password field')
        
        
    @allure.step('Check visible login form') 
    def check_visible(self, email: str = None, password: str = None, is_empty: bool = True):
        
        self.email_label.check_have_text('Email')
        self.email_input.check_visible()
        
        self.password_label.check_have_text('Password')
        self.password_input.check_visible()
        
        if is_empty:
            self.email_input.check_have_value('')
            self.password_input.check_have_value('')
            
        if not is_empty:
            self.email_input.check_have_value(email)
            self.password_input.check_have_value(password)
            
    @allure.step('Fill login form')   
    def fill_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        