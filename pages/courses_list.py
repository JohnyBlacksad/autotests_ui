from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.page_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.creeate_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')
        
        self.empty_course_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_course_descr = page.get_by_test_id('courses-list-empty-view-description-text')
        self.empty_course_icon = page.get_by_test_id('courses-list-empty-view-icon')
        
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_burger_button = page.get_by_test_id('course-view-menu-button')
        self.course_prev_img = page.get_by_test_id('course-preview-image')
        
        self.course_max_score_icon = page.get_by_test_id('course-max-score-info-row-view-icon')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        
        self.course_min_score_icon = page.get_by_test_id('course-min-score-info-row-view-icon')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
    
        self.course_estimated_time_icon = page.get_by_test_id('course-estimated-time-info-row-view-icon')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')
        
        self.course_menu_edit_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_menu_edit_icon = page.get_by_test_id('course-view-edit-menu-item-icon')
        self.course_menu_edit_text = page.get_by_test_id('course-view-edit-menu-item-text')
        
        self.course_menu_del_button = page.get_by_test_id('course-view-delete-menu-item')
        self.course_menu_del_icon = page.get_by_test_id('course-view-delete-menu-item-icon')
        self.course_menu_del_text = page.get_by_test_id('course-view-delete-menu-item-text')
        
        
    def check_page_title(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text('Courses')
        
    def check_empty_result(self):
        expect(self.empty_course_title).to_be_visible()
        expect(self.empty_course_title).to_have_text('There is no results')
        
        expect(self.empty_course_descr).to_be_visible()
        expect(self.empty_course_descr).to_have_text('Results from the load test pipeline will be displayed here')
        
        expect(self.empty_course_icon).to_be_visible()
        
    def check_create_course_button(self):
        expect(self.creeate_course_button).to_be_visible()
    
    def click_create_course(self):
        self.creeate_course_button.click()
        
    def check_visible_course_card(self, 
                                  index: int,
                                  title: str, 
                                  max_score: str, 
                                  min_score: str, 
                                  time: str):
        
        expect(self.course_prev_img.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)
        
        expect(self.course_max_score_icon.nth(index)).to_be_visible()
        expect(self.course_max_score_text.nth(index)).to_be_visible()
        expect(self.course_max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')
        
        expect(self.course_min_score_icon.nth(index)).to_be_visible()
        expect(self.course_min_score_text.nth(index)).to_be_visible()
        expect(self.course_min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')
        
        expect(self.course_estimated_time_icon.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_have_text(f'Estimated time: {time}')
        
    def click_edit_course(self, index: int):
        self.course_burger_button.nth(index).click()
        expect(self.course_menu_edit_icon.nth(index)).to_be_visible()
        expect(self.course_menu_edit_text.nth(index)).to_be_visible()
        expect(self.course_menu_edit_text.nth(index)).to_have_text('Edit')
        self.course_menu_edit_button.nth(index).click()
    
    def click_del_course(self, index: int):
        self.course_burger_button.nth(index).click()
        expect(self.course_menu_del_icon.nth(index)).to_be_visible()
        expect(self.course_menu_del_text.nth(index)).to_be_visible()
        expect(self.course_menu_del_text.nth(index)).to_have_text('Delete')
        self.course_menu_del_button.nth(index).click()
        