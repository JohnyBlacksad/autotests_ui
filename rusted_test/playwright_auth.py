from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    contex = browser.new_context()
    page = contex.new_page()
    
    page.goto()
    
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user@gmail.com')
    
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')
    
    password_input = page.get_by_test_id('registartion-form-password-input').locator('input')
    password_input.fill('password')
    
    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()
    
    contex.storage_state(path='.auth/browser-state.json')
    
    page.wait_for_timeout(5000)
    
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    contex = browser.new_context(storage_state='.auth/browser-state.json')
    page = contex.new_page()
    
    page.goto()