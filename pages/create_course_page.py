from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUplodWidgetComponent
from playwright.sync_api import Page, expect

class CreateCoursePage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.navbar = NavbarComponent(page)
        self.preview_empty_view = EmptyViewComponent(page, 'create-course-preview')
        self.no_task_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUplodWidgetComponent(page, 'create-course-preview')
        
        self.page_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')
        
        # Реализовано в COM EmptyViewComponent
        # self.not_prev_img_course_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        # self.not_prev_img_course_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        # self.not_prev_img_course_descr = page.get_by_test_id('create-course-preview-empty-view-description-text')
        
        
        # Перенесено в COM ImageUplodWidgetComponent
        # self.upload_img_course_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        # self.upload_img_course_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        # self.upload_img_course_desct = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        # self.upload_img_course_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        # self.upload_img_course_button_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')
        # self.remove_img_course_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')
        
        self.title_course_field = page.get_by_test_id('create-course-form-title-input')
        self.title_course_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        
        self.estimated_time_course_field = page.get_by_test_id('create-course-form-estimated-time-input')
        self.estimated_time_course_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        
        self.description_course_field = page.get_by_test_id('create-course-form-description-input')
        self.description_course_input = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        
        self.max_score_course_field = page.get_by_test_id('create-course-form-max-score-input')
        self.max_score_course_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        
        self.min_score_course_field = page.get_by_test_id('create-course-form-min-score-input')
        self.min_score_course_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')
        
        self.task_course_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.task_add_course_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        
        # Реализовано в COM EmptyViewComponent
        # self.not_task_course_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        # self.not_task_course_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        # self.not_task_course_descr = page.get_by_test_id('create-course-exercises-empty-view-description-text')
        
        
    
    def check_title_course(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text('Create course')
        expect(self.create_course_button).to_be_visible()
        expect(self.create_course_button).to_be_disabled()
        
    # Перенес в COM ImageUploadwidgetComponent
    
    # def check_not_image_course_widget(self):
        
    #     self.preview_empty_view.check_visible(
    #         title = 'No image selected', 
    #         description = 'Preview of selected image will be displayed here'
    #         )
        
        # expect(self.not_prev_img_course_icon).to_be_visible()
        # expect(self.not_prev_img_course_title).to_be_visible()
        # expect(self.not_prev_img_course_title).to_have_text('No image selected')
        # expect(self.not_prev_img_course_descr).to_be_visible()
        # expect(self.not_prev_img_course_descr).to_have_text('Preview of selected image will be displayed here')
    
    # Перенес в COM ImageUploadwidgetComponent
    
    # def check_download_img_course_vidget(self):
    #     expect(self.upload_img_course_icon).to_be_visible()
    #     expect(self.upload_img_course_title).to_be_visible()
    #     expect(self.upload_img_course_title).to_have_text('Tap on "Upload image" button to select file')
    #     expect(self.upload_img_course_desct).to_be_visible()
    #     expect(self.upload_img_course_desct).to_have_text('Recommended file size 540X300')
    #     expect(self.upload_img_course_button).to_be_visible()
        
    def check_empty_form_created_course(self):
        expect(self.title_course_field).to_be_visible()
        expect(self.title_course_field.locator('label')).to_have_text('Title')
        expect(self.title_course_input).to_have_value('')
        
        expect(self.estimated_time_course_field).to_be_visible()
        expect(self.estimated_time_course_field.locator('label')).to_have_text('Estimated time')
        expect(self.estimated_time_course_input).to_have_value('')
        
        expect(self.description_course_field).to_be_visible()
        expect(self.description_course_field.locator('label')).to_have_text('Description')
        expect(self.description_course_input).to_have_value('')
        
        expect(self.max_score_course_field).to_be_visible()
        expect(self.max_score_course_field.locator('label')).to_have_text('Max score')
        expect(self.max_score_course_input).to_have_value('0')
        
        expect(self.min_score_course_field).to_be_visible()
        expect(self.min_score_course_field.locator('label')).to_have_text('Min score')
        expect(self.min_score_course_input).to_have_value('0')
        
    def check_empty_task_list(self):
        expect(self.task_course_title).to_be_visible()
        expect(self.task_course_title).to_have_text('Exercises')
        expect(self.task_add_course_button).to_be_visible()
        expect(self.task_add_course_button).to_be_enabled()
        
        self.no_task_empty_view.check_visible(
            title = 'There is no exercises',
            description= 'Click on "Create exercise" button to create new exercise'
        )
        
        # Реализовано в COM
        # expect(self.not_task_course_icon).to_be_visible()
        # expect(self.not_task_course_title).to_be_visible()
        # expect(self.not_task_course_title).to_have_text('There is no exercises')
        # expect(self.not_task_course_descr).to_be_visible()
        # expect(self.not_task_course_descr).to_have_text('Click on "Create exercise" button to create new exercise')
        
        
    # Перенес в COM ImageUploadwidgetComponent
    
    # def remove_course_img(self):
    #     self.remove_img_course_button.click()
    #     self.check_not_image_course_widget()


    def fill_course_form(self, title: str,
                         time: str,
                         description: str,
                         max_score: str,
                         min_score: str):
        
        self.title_course_input.fill(title)
        self.estimated_time_course_input.fill(time)
        self.description_course_input.fill(description)
        self.max_score_course_input.fill(max_score)
        self.min_score_course_input.fill(min_score)
        
        expect(self.title_course_input).to_have_value(title)
        expect(self.estimated_time_course_input).to_have_value(time)
        expect(self.description_course_input).to_have_value(description)
        expect(self.max_score_course_input).to_have_value(max_score)
        expect(self.min_score_course_input).to_have_value(min_score)
        expect(self.create_course_button).to_be_enabled()
        
        
    def click_created_task_course(self):
        self.task_add_course_button.click()
        
    def check_visible_task_form(self, index: int):
        task_title_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        task_title_field = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        
        task_descr_input = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')
        task_descr_field = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')
        
        task_delete_button = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        
        expect(task_title_field).to_be_visible()
        expect(task_title_field.locator('label')).to_have_text('Title')
        expect(task_title_input).to_have_value('Exercise title')
        
        expect(task_descr_field).to_be_visible()
        expect(task_descr_field.locator('label')).to_have_text('Description')
        expect(task_descr_input).to_have_value('Exercise description')
        
        expect(task_delete_button).to_be_visible()
        
    def fill_task_form_course(self, title_task: str, 
                              descr_task: str, 
                              index: int):
        
        task_title_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')
        task_descr_input = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')
        
        task_title_input.fill(title_task)
        task_descr_input.fill(descr_task)
        
        expect(task_title_input).to_have_value(title_task)
        expect(task_descr_input).to_have_value(descr_task)
        
    def click_created_course(self):
        self.create_course_button.click()

