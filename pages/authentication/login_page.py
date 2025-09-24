from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page
import re

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form = LoginFormComponent(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'Title')
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.error_allert = Text(page, 'login-page-wrong-email-or-password-alert', 'Wrong email or password')
        
    def check_visible(self, email: str = None, password: str = None, is_empty: bool = True):
        self.title.check_visible()
        self.title.check_have_text('UI Course')
        self.registration_link.check_visible()
        self.registration_link.check_have_text('Registration')
        self.login_button.check_visible()
        self.login_button.check_have_text('Login')
           
        if is_empty:
            self.login_form.check_visible(email=email, password=password, is_empty=is_empty)
            self.login_button.check_disabled()
                
        if not is_empty:
            self.login_form.check_visible()
            self.login_button.check_enabled()
    
    def click_login_button(self) -> None:
        self.login_button.click()
        
    def click_registration_link(self) -> None:
        self.registration_link.click()
        self.check_current_url(re.compile(r'.*/#/auth/registration'))
    
    def check_allert_visible(self):
        self.error_allert.check_visible()
        self.error_allert.check_have_text('Wrong email or password')
    