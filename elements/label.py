from elements.base_element import BaseElement
from playwright.sync_api import expect


class Label(BaseElement):
    def get_locator(self, **kwargs):
        return super().get_locator(**kwargs).locator('label')
    
    def check_have_text(self, value: str, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(value)
    