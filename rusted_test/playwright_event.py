from playwright.sync_api import sync_playwright, Request, Response

def log_request(requset: Request):
    print(f'Request: {requset.url}')

def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')
    
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', 
              wait_until='networkidle')
    
    page.on('request', log_request)
    page.remove_listener('request', log_request)
    page.on('response', log_response)
    
    page.wait_for_timeout(5000)