from pages.login_page import LoginPage
import pytest

users = {('user.name@gmail.com', 'password'): 'Invalid creeds',
        ('user.name@gmail.com', '  '): 'Two spaces in password', 
        ('  ', 'password'): 'Two spaces in email'}


@pytest.mark.authorization
@pytest.mark.parametrize('email, password', 
                         users.keys(),
                         ids=users.values())
def test_wrong_email_or_password_authorization(login_page: LoginPage, 
                                               email: str, 
                                               password: str):
    
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.fill_login_form(emai=email, password=password)
    login_page.click_login_button()
    login_page.check_allert_visible()