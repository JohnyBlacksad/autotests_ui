from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.page_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')
        
        self.not_prev_img_course_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.not_prev_img_course_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.not_prev_img_course_descr = page.get_by_test_id('create-course-preview-empty-view-description-text')
        
        self.upload_img_course_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_img_course_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_img_course_desct = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.upload_img_course_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_img_course_button_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')
        self.remove_img_course_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')
        
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
        
        self.not_task_course_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.not_task_course_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.not_task_course_descr = page.get_by_test_id('create-course-exercises-empty-view-description-text')
        
        self.is_image_uploaded = False
        
    
    def check_title_course(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text('Create course')
        expect(self.create_course_button).to_be_visible()
        expect(self.create_course_button).to_be_disabled()
        
    def check_not_image_course_widget(self):
        expect(self.not_prev_img_course_icon).to_be_visible()
        expect(self.not_prev_img_course_title).to_be_visible()
        expect(self.not_prev_img_course_title).to_have_text('No image selected')
        expect(self.not_prev_img_course_descr).to_be_visible()
        expect(self.not_prev_img_course_descr).to_have_text('Preview of selected image will be displayed here')
    
    def check_download_img_course_vidget(self):
        expect(self.upload_img_course_icon).to_be_visible()
        expect(self.upload_img_course_title).to_be_visible()
        expect(self.upload_img_course_title).to_have_text('Tap on "Upload image" button to select file')
        expect(self.upload_img_course_desct).to_be_visible()
        expect(self.upload_img_course_desct).to_have_text('Recommended file size 540X300')
        expect(self.upload_img_course_button).to_be_visible()
        
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
        expect(self.max_score_course_input).to_have_value('')
        
        expect(self.min_score_course_field).to_be_visible()
        expect(self.min_score_course_field.locator('label')).to_have_text('Min score')
        expect(self.min_score_course_input).to_have_value('')
        
    def check_empty_task_list(self):
        expect(self.task_course_title).to_be_visible()
        expect(self.task_course_title).to_have_text('Exercises')
        expect(self.task_add_course_button).to_be_visible()
        expect(self.task_add_course_button).to_be_enabled()
        expect(self.not_task_course_icon).to_be_visible()
        expect(self.not_task_course_title).to_be_visible()
        expect(self.not_task_course_title).to_have_text('There is no exercises')
        expect(self.not_task_course_descr).to_be_visible()
        expect(self.not_task_course_descr).to_have_text('Click on "Create exercise" button to create new exercise')
        
    def upload_course_img(self, file: str):
        self.upload_img_course_button_input.set_input_files(file)
        expect(self.page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')).to_be_visible()
        
    def remove_course_img(self):
        self.remove_img_course_button.click()
        self.check_not_image_course_widget()