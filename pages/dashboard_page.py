from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        
        self.navbar = NavbarComponent(page)
        self.side_bar = SidebarComponent(page)
        self.toolbar = DashboardToolbarViewComponent(page)
        self.chart_students = ChartViewComponent(page, 'students', 'bar')
        self.chart_activites = ChartViewComponent(page, 'activities', 'line')
        self.chart_courses = ChartViewComponent(page, 'courses', 'pie')
        self.chart_scores = ChartViewComponent(page, 'scores', 'scatter')
        
        
    def check_students_chart(self):
        self.chart_students.check_visible('Students')
        
    def check_activities_chart(self):
        self.chart_activites.check_visible('Activities')
    
    def check_courses_chart(self):
        self.chart_courses.check_visible('Courses')
    
    def check_scores_chart(self):
        self.chart_scores.check_visible('Scores')