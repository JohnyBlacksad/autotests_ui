from components.base_component import BaseComponent
from elements.textarea import Textarea
from elements.input import Input
from playwright.sync_api import Page

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.title = Input(page, 'create-course-form-title-input', 'Title')
        self.estimated_time = Input(page, 'create-course-form-estimated-time-input', "Estimated time")
        self.description = Textarea(page, 'create-course-form-description-input', 'Description')
        self.max_score = Input(page, 'create-course-form-max-score-input', 'Max score')
        self.min_score = Input(page, 'create-course-form-min-score-input', 'Min score')
        
    def fill(
            self, 
            title: str,
            estimated_time: str, 
            description: str, 
            max_score: int, 
            min_score: int
            ):
        
        self.title.fill(title)
        self.estimated_time.fill(estimated_time)
        self.description.fill(description)
        self.max_score.fill(max_score)
        self.min_score.fill(min_score)
        
        self.title.check_have_value(title)
        self.estimated_time.check_have_value(estimated_time)
        self.description.check_have_text(description)
        self.max_score.check_have_value(max_score)
        self.min_score.check_have_value(min_score)
        
    def check_visible(self):
        self.title.check_visible()
        self.estimated_time.check_visible()
        self.description.check_visible()
        self.max_score.check_visible()
        self.min_score.check_visible()
        
        self.title.check_have_value('')
        self.estimated_time.check_have_value('')
        self.description.check_have_text('')
        self.max_score.check_have_value('0')
        self.min_score.check_have_value('0')
        