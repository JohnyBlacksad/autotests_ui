from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.text import Text
from elements.button import Button
from elements.link import Link
from playwright.sync_api import Page

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)
        
        self.title = Text(page, 'authentication-ui-course-title-text', 'Registration page Title')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login link')
        
    def fill_registration_form(self, email: str, 
                               username: str, 
                               password: str) -> None:
        
        self.registration_form.check_visible(is_empty=True)
        self.registration_form.fill_form(email=email, username=username, password=password)
        self.registration_form.check_visible(email=email, username=username, password=password, is_empty=False)
        
    def click_reg_button(self) -> None:
        self.registration_button.check_enabled()
        self.registration_button.click()
        
    def click_login_link(self) -> None:
        self.login_link.click()
        
    def check_title(self) -> None:
        self.title.check_visible()
        self.title.check_have_text('UI Course')
        