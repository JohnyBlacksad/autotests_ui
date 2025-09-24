from components.base_component import BaseComponent
from components.navigation.side_bar_list_item import SideBarListItemComponents
from playwright.sync_api import Page
import re

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.logout = SideBarListItemComponents(page, 'logout')
        self.courses = SideBarListItemComponents(page, 'courses')
        self.dashboard = SideBarListItemComponents(page, 'dashboard')
        
    def check_visible(self):
        self.logout.check_visible('Logout')
        self.courses.check_visible('Courses')
        self.dashboard.check_visible('Dashboard')
        
    def click_logout(self):
        self.logout.navigate(re.compile(r'.*/#/auth/login'))
        
    def click_courses(self):
        self.courses.navigate(re.compile(r'.*/#/courses'))
        
    def click_dashboard(self):
        self.dashboard.navigate(re.compile(r'.*/#/dashboard'))