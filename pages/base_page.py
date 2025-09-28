from playwright.sync_api import Page, expect
from typing import Pattern
from tools.logger import get_logger
import allure

logger = get_logger('BASE PAGE')

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
    
    def visit(self, url: str) -> None:
        step = f'Opening the URL: "{url}"'
        
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')
        
    def reload(self):
        step = f'Reloading page: "{self.page.url}"'
        
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='networkidle')
        
    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern: "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)