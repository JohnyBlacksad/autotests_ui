from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    
    email_input = page.get_by_test_id('registration-form-email-input').locator('//input')
    email_input.fill("user.name@gmail.com")
    
    username_input = page.get_by_test_id('registration-form-username-input').locator('//input')
    username_input.fill('username')
    
    password_input = page.get_by_test_id('registration-form-password-input').locator('//input')
    password_input.fill('password')
    
    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()
    
    page.wait_for_timeout(3000)
    
    title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title).to_be_visible()
    expect(title).to_have_text('Dashboard')
    
    page.wait_for_timeout(3000)