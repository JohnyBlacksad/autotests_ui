from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.authorization
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', 
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