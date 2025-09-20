from pages.login_page import LoginPage
import pytest

#Переписал функцию согласно задаче, изменил способ получения локаторов и заголовок функции.

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
    #------------------------------------------------
    #Вынесли логику поиска локаторов в POM
    
    #chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    
    #email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    #email_input.fill('user.name@gmail.com')
    
    #password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    #password_input.fill('password')
    
    #login_button = chromium_page.get_by_test_id('login-page-login-button')
    #login_button.click()
    
    #wrong_allert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    #expect(wrong_allert).to_be_visible()
    #expect(wrong_allert).to_have_text('Wrong email or password')