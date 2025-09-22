from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from typing import Pattern

class SideBarListItemComponents(BaseComponent):
    def __init__(self, page: Page, identifire: str):
        super().__init__(page)
        
        self.icon = page.get_by_test_id(f'{identifire}-drawer-list-item-icon')
        self.text = page.get_by_test_id(f'{identifire}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{identifire}-drawer-list-item-button')
        
    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()
        
        expect(self.text).to_be_visible()
        expect(self.text).to_have_text(title)
        
        expect(self.button).to_be_visible()
        
    def navigate(self, url: Pattern[str]):
        self.button.click()
        self.check_current_url()