from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.text import Text
from elements.image import Image
from elements.icon import Icon
from playwright.sync_api import Page
import allure

class CourseViewComponents(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_menu = CourseViewMenuComponent(page)
        
        self.img = Image(page, 'course-preview-image', 'Preview image')
        
        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')
        
        self.max_score_icon = Icon(page, 'course-max-score-info-row-view-icon', 'Icon')
        self.min_score_icon = Icon(page, 'course-min-score-info-row-view-icon', 'Icon')
        self.estimated_time_icon = Icon(page, 'course-estimated-time-info-row-view-icon', 'Icon')
    
    @allure.step('Check visible at index "{index}"')
    def check_visible(
                self, 
                index: int,
                title: str,
                max_score: int,
                min_score: int,
                estimated_time: str
            ):
        
        self.cart_menu.menu_button.check_visible(nth=index)
        
        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)
        
        self.img.check_visible(nth=index)
        
        self.max_score_icon.check_visible(nth=index)
        self.max_score_text.check_visible(nth=index)
        self.max_score_text.check_have_text(f'Max score: {max_score}', nth=index)
        
        self.min_score_icon.check_visible(nth=index)
        self.min_score_text.check_visible(nth=index)
        self.min_score_text.check_have_text(f'Min score: {min_score}', nth=index)
        
        self.estimated_time_icon.check_visible(nth=index)
        self.estimated_time_text.check_visible(nth=index)
        self.estimated_time_text.check_have_text(f'Estimated time: {estimated_time}', nth=index)
        
        