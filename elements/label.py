from elements.base_element import BaseElement
from playwright.sync_api import expect
from tools.logger import get_logger
import allure

logger = get_logger('LABEL')

class Label(BaseElement):
    @property
    def type_of(self) -> str:
        return 'label'
    
    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator('label')
    
    def check_have_text(self, value: str, nth: int = 0, **kwargs) -> None:
        step = f'Checking {self.type_of} "{self.name}" have a text "{value}"'
        
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(value)
    