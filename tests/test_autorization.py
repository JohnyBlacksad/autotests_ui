from playwright.sync_api import expect, Page
import pytest

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
        expect(error_locator).to_have_text("Wrong email or password")
        