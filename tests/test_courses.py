from pages.courses_list import CoursesListPage
import pytest
import re

@pytest.mark.regression
@pytest.mark.authorization
def test_empty_courses_list(courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_empty_result()
        courses_list_page.navbar.check_visible('username')
        courses_list_page.navbar.check_current_url(re.compile(r'.*/#/courses'))
        courses_list_page.side_bar.check_visible()
        
        