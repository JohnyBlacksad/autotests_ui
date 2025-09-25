from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from playwright.sync_api import Page
import allure

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Button')
        
    @allure.step('Check visible create course exercises toolbar')
    def check_visible(self):
        self.title.check_visible()
        self.create_exercise_button.check_visible()
        self.create_exercise_button.check_enabled()
        
        
    def click_add_exercise_button(self):
        self.create_exercise_button.click()