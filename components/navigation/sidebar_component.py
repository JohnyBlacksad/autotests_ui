from components.base_component import BaseComponent
from components.navigation.side_bar_list_item import SideBarListItemComponents
from playwright.sync_api import Page
import re
import allure

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.logout = SideBarListItemComponents(page, 'logout')
        self.courses = SideBarListItemComponents(page, 'courses')
        self.dashboard = SideBarListItemComponents(page, 'dashboard')
    
    @allure.step('Check visible sidebar')  
    def check_visible(self):
        self.logout.check_visible('Logout')
        self.courses.check_visible('Courses')
        self.dashboard.check_visible('Dashboard')
        
    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout.navigate(re.compile(r'.*/#/auth/login'))
    
    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses.navigate(re.compile(r'.*/#/courses'))
    
    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard.navigate(re.compile(r'.*/#/dashboard'))