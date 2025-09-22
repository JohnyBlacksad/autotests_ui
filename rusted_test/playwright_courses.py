from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration', 
              wait_until='networkidle')
    
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('username@gmail.com')
    
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')
    
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')
    
    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()
    
    context.storage_state(path='.auth/browser-state.json')
    
    
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context(storage_state='.auth/browser-state.json')
    page = context.new_page()
    
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', 
              wait_until='networkidle')
    
    title_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_text).to_have_text('Courses')
    
    result_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_text).to_have_text('There is no results')
    
    icon_img = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_img).to_be_visible()
    
    result_descr = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_descr).to_be_visible()
    expect(result_descr).to_have_text('Results from the load test pipeline will be displayed here')
    print('Test successful')