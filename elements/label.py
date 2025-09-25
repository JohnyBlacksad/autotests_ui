from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure

class Label(BaseElement):
    @property
    def type_of(self) -> str:
        return 'label'
    
    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator('label')
    
    def check_have_text(self, value: str, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Checking {self.type_of} "{self.name}" have a text "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(value)
    