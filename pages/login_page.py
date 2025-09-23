from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form = LoginFormComponent(page)
       
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.error_allert = Text(page, 'login-page-wrong-email-or-password-alert', 'Wrong email or password')
        
    def click_login_button(self) -> None:
        self.login_button.click()
        
    def click_registration_link(self) -> None:
        self.registration_link.click()
    
    def check_allert_visible(self):
        self.error_allert.check_visible()
        self.error_allert.check_have_text('Wrong email or password')
    