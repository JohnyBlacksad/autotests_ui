from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    
    email_locator = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    password_locator = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    button_locator = page.locator('//button[@data-testid="login-page-login-button"]')
    error_locator = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    
    email_locator.fill("user.name@gmail.com")
    password_locator.fill("password")
    button_locator.click()
    
    expect(error_locator).to_be_visible()
    expect(error_locator).to_have_text("Wrong email or password")
    
    page.wait_for_timeout(5000)