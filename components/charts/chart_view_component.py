from components.base_component import BaseComponent
from elements.text import Text
from elements.image import Image
from playwright.sync_api import Page
import allure

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifire: str, chart_type: str):
        super().__init__(page)
        
        self.title = Text(page, f'{identifire}-widget-title-text', 'Title chart')
        self.chart = Image(page, f'{identifire}-{chart_type}-chart', 'Chart view')
    
    @allure.step('Check visible chart "{title}" widget')
    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)
        self.chart.check_visible()