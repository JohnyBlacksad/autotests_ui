from pages.create_course_page import CreateCoursePage
from pages.courses_list import CoursesListPage
import pytest

@pytest.mark.regression
@pytest.mark.course
@pytest.mark.parametrize('course_title, course_time, course_descr, course_max_score, course_min_score, course_task_title, course_task_descr', 
                         [('Playwright', '2 weeks', 'Playwright', '100', '10', 'Task 1', 'This is task 1')])
def test_create_course(created_courses_page: CreateCoursePage, 
                       courses_list_page: CoursesListPage,
                       course_title: str, 
                       course_time: str, 
                       course_descr: str,
                       course_max_score: int,
                       course_min_score: int,
                       course_task_title: str,
                       course_task_descr: str):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.toolbar_view.click_create_course_button()
    
    created_courses_page.check_title_course()
    created_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
    created_courses_page.check_empty_form_created_course()
    created_courses_page.check_empty_task_list()
    created_courses_page.image_upload_widget.upload_course_img(file='./testdata/files/image.jpg')
    created_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
    
    created_courses_page.fill_course_form(title=course_title,
                                          time=course_time,
                                          description=course_descr,
                                          max_score=course_max_score,
                                          min_score=course_min_score)
    
    created_courses_page.click_created_task_course()
 
    
    created_courses_page.check_visible_task_form(index=0)
    created_courses_page.fill_task_form_course(title_task=course_task_title,
                                               descr_task=course_task_descr,
                                               index=0)
    
    created_courses_page.click_created_course()
    courses_list_page.course_view.check_visible(index=0, 
                                                title=course_title,
                                                max_score=course_max_score,
                                                min_score=course_min_score,
                                                estimated_time=course_time)
    courses_list_page.course_view.cart_menu.cilck_delete(index=0)