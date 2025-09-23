from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUplodWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from playwright.sync_api import Page

class CreateCoursePage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.navbar = NavbarComponent(page)
        self.toolbar = CreateCourseToolbarViewComponent(page)
        self.exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.preview_empty_view = EmptyViewComponent(page, 'create-course-preview')
        self.no_task_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUplodWidgetComponent(page, 'create-course-preview')
        self.course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.course_form = CreateCourseFormComponent(page)
        
        self.task_delete_button = page.get_by_test_id('create-course-exercise-0-box-toolbar-delete-exercise-button')
        
    def check_empty_task_list(self):
        self.exercises_toolbar.check_visible()
        self.no_task_empty_view.check_visible(
            title = 'There is no exercises',
            description= 'Click on "Create exercise" button to create new exercise'
        )
        
             
