from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from elements.file_input import FileInput
from playwright.sync_api import Page
import allure

class ImageUplodWidgetComponent(BaseComponent):
    def __init__(self, page: Page,  identifier: str):
        super().__init__(page)
        
        self.preview_empty_view = EmptyViewComponent(page, identifier)
        
        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview course image')
        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', 'Upload icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Title on upload widget')
        self.image_upload_info_description = Text(page, f'{identifier}-image-upload-widget-info-description-text', 'Description on upload widget')
        
        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload button')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove button')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload file field')
        
    
    @allure.step('Check visible upload preview image widget')
    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')
        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')
        self.upload_button.check_visible()
        
        if is_image_uploaded:
            self.preview_image.check_visible()
            self.remove_button.check_visible()
        
        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title = 'No image selected', 
                description = 'Preview of selected image will be displayed here'
            )
        
    def upload_course_img(self, file: str):
        self.upload_input.set_input_files(file=file)
        
        
    def remove_image(self):
        self.remove_button.click()
        