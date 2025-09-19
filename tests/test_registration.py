from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
import pytest

@pytest.mark.parametrize('email, username, password', 
                         [('user.name@gmail.com', 'username', 'password')])
def test_succesful_registration(registration_page: RegistrationPage,
                                dashboard_page: DashboardPage, 
                                email: str, 
                                username: str, 
                                password: str) -> None:
    
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.check_title()
    
    registration_page.fill_registration_form(email=email, 
                                             username=username, 
                                             password=password)
    
    registration_page.click_reg_button()
    dashboard_page.check_page_title()