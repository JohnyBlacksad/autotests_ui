from components.base_component import BaseComponent
from elements.input import Input
from elements.label import Label
from playwright.sync_api import Page
import allure

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.email_label = Label(page, 'registration-form-email-input', 'Email placeholder')
        self.email_input = Input(page, 'registration-form-email-input', 'Email field')
        
        self.username_label = Label(page, 'registration-form-username-input', 'Username placeholder')
        self.username_input = Input(page, 'registration-form-username-input', 'Username field')
        
        self.password_label = Label(page, 'registration-form-password-input', 'Password placeholder')
        self.password_input = Input(page, 'registration-form-password-input', 'Password field')
    
    @allure.step('Check visible registration form')
    def check_visible(
                self, 
                email: str = None, 
                username: str = None, 
                password: str = None, 
                is_empty: bool = True
                ):
        
        self.email_input.check_visible()
        self.email_label.check_have_text('Email')
        self.username_input.check_visible()
        self.username_label.check_have_text('Username')
        self.password_input.check_visible()
        self.password_label.check_have_text('Password')
        
        if is_empty:
            self.email_input.check_have_value('')
            self.username_input.check_have_value('')
            self.password_input.check_have_value('')
        
        if not is_empty:
            self.email_input.check_have_value(email)
            self.username_input.check_have_value(username)
            self.password_input.check_have_value(password)
            
    @allure.step('Fill registration form')
    def fill_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)