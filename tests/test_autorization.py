from playwright.sync_api import expect, Page
import pytest

#Переписал функцию согласно задаче, изменил способ получения локаторов и заголовок функции.

""" 
@pytest.mark.regression
@pytest.mark.authorization
def test_authorization(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        
        email_locator = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        password_locator = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        button_locator = chromium_page.locator('//button[@data-testid="login-page-login-button"]')
        error_locator = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        
        email_locator.fill("user.name@gmail.com")
        password_locator.fill("password")
        button_locator.click()
        
        expect(error_locator).to_be_visible()
        expect(error_locator).to_have_text("Wrong email or password") """
        


users = {('user.name@gmail.com', 'password'): 'Invalid creeds',
        ('user.name@gmail.com', '  '): 'Two spaces in password', 
        ('  ', 'password'): 'Two spaces in email'}

@pytest.mark.authorization
@pytest.mark.parametrize('email, password', 
                         users.keys(),
                         ids=users.values())
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')
        
        password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill('password')
        
        login_button = chromium_page.get_by_test_id('login-page-login-button')
        login_button.click()
        
        wrong_allert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_allert).to_be_visible()
        expect(wrong_allert).to_have_text('Wrong email or password')