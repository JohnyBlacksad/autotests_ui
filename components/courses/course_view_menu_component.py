from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import re

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_button = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_button = page.get_by_test_id('course-view-delete-menu-item')
        
        self.edit_button_icon = page.get_by_test_id('course-view-edit-menu-item-icon')
        self.delete_button_icon = page.get_by_test_id('course-view-delete-menu-item-icon')
        
        self.edit_button_text = page.get_by_test_id('course-view-edit-menu-item-text')
        self.delete_button_text = page.get_by_test_id('course-view-delete-menu-item-text')
        
    def click_edit(self, index: int):
        self.menu_button.nth(index).click()
        expect(self.edit_button_icon.nth(index)).to_be_visible()
        expect(self.edit_button_text.nth(index)).to_have_text('Edit')
        self.edit_button.nth(index).click()
        
    def cilck_delete(self, index: int):
        self.menu_button.nth(index).click()
        expect(self.delete_button_icon.nth(index)).to_be_visible()
        expect(self.delete_button_text.nth(index)).to_have_text('Delete')
        self.delete_button.nth(index).click()
        