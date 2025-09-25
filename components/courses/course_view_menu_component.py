from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text
from playwright.sync_api import Page
import allure


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.menu_button = Button(page, 'course-view-menu-button', 'Button')
        self.edit_button = Button(page, 'course-view-edit-menu-item', 'Button')
        self.delete_button = Button(page, 'course-view-delete-menu-item', 'Button')
        
        self.edit_button_icon = Icon(page, 'course-view-edit-menu-item-icon', 'Icon')
        self.delete_button_icon = Icon(page, 'course-view-delete-menu-item-icon', 'Icon')
        
        self.edit_button_text = Text(page, 'course-view-edit-menu-item-text', 'Text')
        self.delete_button_text = Text(page, 'course-view-delete-menu-item-text', 'Text')
    
    @allure.step('Open course menu at index "{index}" and click edit button')
    def click_edit(self, index: int):
        self.menu_button.check_visible(nth=index)
        self.menu_button.click(nth=index)
        self.edit_button_icon.check_visible(nth=index)
        self.edit_button_text.check_have_text('Edit', nth=index)
        self.edit_button.click(nth=index)
    
    @allure.step('Open course menu at index "{index}" and click delete button')
    def cilck_delete(self, index: int):
        self.menu_button.check_visible(nth=index)
        self.menu_button.click(nth=index)
        self.delete_button.check_visible(nth=index)
        self.delete_button_icon.check_visible(nth=index)
        self.delete_button_text.check_have_text('Delete', nth=index)
        self.delete_button.click(nth=index)