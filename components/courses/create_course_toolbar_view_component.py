from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_button = page.get_by_test_id('create-course-toolbar-create-course-button')
        
    def check_visible(self, is_form_fill: bool = False):
        expect(self.title).to_be_visible()
        expect(self.create_button).to_be_visible()
        
        if is_form_fill:
            expect(self.create_button).to_be_enabled()
            
        if not is_form_fill:
            expect(self.create_button).to_be_disabled()
            
    def click_create_button(self):
        self.create_button.click()