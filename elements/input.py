from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure

class Input(BaseElement):
    
    @property
    def type_of(self) -> str:
        return 'input'
    
    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator('input')
    
    def fill(self, value: str, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)
        
    def check_have_value(self, value: str, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Checking {self.type_of} "{self.name}" have a value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)