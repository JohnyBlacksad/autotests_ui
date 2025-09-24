from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from playwright.sync_api import Page

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course button')
        
    def check_visible(self, is_form_fill: bool = False):
        self.title.check_visible()
        self.create_button.check_visible()
        
        if is_form_fill:
           self.create_button.check_enabled()
            
        if not is_form_fill:
            self.create_button.check_disabled()
            
    def click_create_button(self):
        self.create_button.click()