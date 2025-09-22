from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        
        self.navbar = NavbarComponent(page)
        self.side_bar = SidebarComponent(page)
        self.title = page.get_by_test_id('dashboard-toolbar-title-text')
        
        self.student_title = page.get_by_test_id('students-widget-title-text')
        self.student_widget = page.get_by_test_id('students-bar-chart')
        
        self.activities_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_widget = page.get_by_test_id('activities-line-chart')
        
        self.courses_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_widget = page.get_by_test_id('courses-pie-chart')
       
        self.scores_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_widget = page.get_by_test_id('scores-scatter-chart')
        
    def check_page_title(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')
        
    def check_students_chart(self):
        expect(self.student_title).to_be_visible()
        expect(self.student_title).to_have_text('Students')
        expect(self.student_widget).to_be_visible()
        
    def check_activities_chart(self):
        expect(self.activities_title).to_be_visible()
        expect(self.activities_title).to_have_text('Activities')
        expect(self.activities_widget).to_be_visible()
    
    def check_courses_chart(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')
        expect(self.activities_widget).to_be_visible()
    
    def check_scores_chart(self):
        expect(self.scores_title).to_be_visible()
        expect(self.scores_title).to_have_text('Scores')
        expect(self.scores_widget).to_be_visible()