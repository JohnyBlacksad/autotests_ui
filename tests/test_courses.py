from pages.courses_list import CoursesListPage
import pytest
import re

@pytest.mark.regression
@pytest.mark.authorization
def test_empty_courses_list(courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.check_page_title()
        courses_list_page.check_empty_result()
        courses_list_page.check_create_course_button()
        courses_list_page.navbar.check_visible('username')
        courses_list_page.navbar.check_current_url(re.compile(r'.*/#/courses'))
        courses_list_page.side_bar.check_visible()
        
        """ chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', 
                wait_until='networkidle')
        
        title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_text).to_have_text('Courses')
        
        result_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_text).to_have_text('There is no results')
        
        icon_img = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_img).to_be_visible()
        
        result_descr = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_descr).to_be_visible()
        expect(result_descr).to_have_text('Results from the load test pipeline will be displayed here')
        """