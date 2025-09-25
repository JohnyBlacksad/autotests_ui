from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
import pytest
import allure



uncorrect_users = {('user.name@gmail.com', 'password'): 'Invalid creeds',
        ('user.name@gmail.com', '  '): 'Two spaces in password', 
        ('  ', 'password'): 'Two spaces in email'}

correct_users = {('test@gmail.com', 'testUser', 'password'): 'First correct user'}

@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
class TestAutorization:
    @pytest.mark.parametrize('email, username, password', correct_users.keys(), ids=correct_users.values())
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with correct email or password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, registration_page: RegistrationPage, 
                                 dashboard_page: DashboardPage,
                                 login_page: LoginPage, 
                                 email: str, username: str, password:str):
        
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.check_title()
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_reg_button()
        
        dashboard_page.navbar.check_visible(username=username)
        dashboard_page.toolbar.check_visible()
        dashboard_page.side_bar.check_visible()
        dashboard_page.side_bar.click_logout()
        
        login_page.login_form.check_visible()
        login_page.login_form.fill_form(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password, is_empty=False)
        login_page.click_login_button()
        
        dashboard_page.navbar.check_visible(username=username)
        dashboard_page.toolbar.check_visible()
        dashboard_page.side_bar.check_visible()
        
        
    @pytest.mark.parametrize('email, password', 
                         uncorrect_users.keys(),
                         ids=uncorrect_users.values())
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with wrong email or password')
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, 
                                               email: str, 
                                               password: str):
    
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.check_visible()
        login_page.login_form.fill_form(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password, is_empty=False)
        login_page.click_login_button()
        login_page.check_allert_visible()
    
    @allure.tag(AllureTag.NAVIGATION)
    @allure.title('Navigation from login page to registration page')
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, 
                                                         registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.check_visible()
        login_page.click_registration_link()
        registration_page.check_title()
        registration_page.registration_form.check_visible()