from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    
    unknow = page.locator('#unknow')
    expect(unknow).to_be_visible()
    
    login_button = page.locator('login-page-login-button')
    login_button.fill('asdf')
    
    