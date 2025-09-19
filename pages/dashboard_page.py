from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        
        self.title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.student_table_title = page.get_by_test_id('students-widget-title-text')
        self.activities_table_title = page.get_by_test_id('activities-widget-title-text')
        self.courses_table_title = page.get_by_test_id('courses-widget-title-text')
        self.scores_table_title = page.get_by_test_id('scores-widget-title-text')
        
    def check_page_title(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')