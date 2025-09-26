from components.base_component import BaseComponent
from elements.text import Text
from playwright.sync_api import Page
import allure

class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'Title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome message')
        
    @allure.step("Check visible navigationbar and 'welcome {username}' message")
    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')
        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')