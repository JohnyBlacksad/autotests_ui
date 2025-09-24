from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.button import Button
from elements.icon import Icon
from elements.text import Text
from typing import Pattern

class SideBarListItemComponents(BaseComponent):
    def __init__(self, page: Page,  identifier: str):
        super().__init__(page)
        
        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Sidebar icon')
        self.text = Text(page, f'{identifier}-drawer-list-item-title-text', 'Text')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Menu button')
        
    def check_visible(self, title):
        self.icon.check_visible()
        self.text.check_visible()
        self.text.check_have_text(title)
        
    def navigate(self, url: Pattern[str]):
        self.button.click()
        self.check_current_url()