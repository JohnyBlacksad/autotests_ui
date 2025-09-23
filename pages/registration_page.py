from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from playwright.sync_api import Page, expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)
        
        self.title = page.get_by_test_id('authentication-ui-course-title-text')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        
    def fill_registration_form(self, email: str, 
                               username: str, 
                               password: str) -> None:
        
        self.registration_form.check_visible(is_empty=True)
        self.registration_form.fill_form(email=email, username=username, password=password)
        self.registration_form.check_visible(email=email, username=username, password=password, is_empty=False)
        
    def click_reg_button(self) -> None:
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()
        
    def click_login_link(self) -> None:
        self.login_link.click()
        
    def check_title(self) -> None:
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('UI Course')