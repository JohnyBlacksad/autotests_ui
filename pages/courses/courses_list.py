from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponents
from pages.base_page import BasePage
from playwright.sync_api import Page
import re

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.side_bar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponents(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        
        
    def check_empty_result(self):
        title = 'There is no results'
        description = 'Results from the load test pipeline will be displayed here'
        
        self.empty_view.check_visible(title=title, description=description)
        
    def check_courses_list(self, index: int, title: str, max_score: int, min_score: int, estimated_time: str):
        self.side_bar.check_visible()
        self.course_view.check_visible(index=index, title=title, max_score=max_score, min_score=min_score, estimated_time=estimated_time)
        self.toolbar_view.check_visible()
        
    def click_edit_course(self, index: int):
        self.course_view.cart_menu.click_edit(index=index)
        self.check_current_url(re.compile(r'.*/#/courses/[^/#]+$'))