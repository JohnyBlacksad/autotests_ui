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
    courses_list_page.click_create_course()
    
    created_courses_page.check_title_course()
    created_courses_page.check_not_image_course_widget()
    created_courses_page.check_not_image_course_widget()
    created_courses_page.check_download_img_course_vidget()
    created_courses_page.check_empty_form_created_course()
    created_courses_page.check_empty_task_list()
    created_courses_page.upload_course_img(file='./testdata/files/image.jpg')
    
    created_courses_page.fill_course_form(title=course_title,
                                          time=course_time,
                                          description=course_descr,
                                          max_score=course_max_score,
                                          min_score=course_min_score)
    
    created_courses_page.click_created_task_course()
    index = 0
    
    created_courses_page.check_visible_task_form(index)
    created_courses_page.fill_task_form_course(title_task=course_task_title,
                                               descr_task=course_task_descr,
                                               index=index)
    
    created_courses_page.click_created_course()
    courses_list_page.check_visible_course_card(index=0, 
                                                title=course_title,
                                                max_score=course_max_score,
                                                min_score=course_min_score,
                                                time=course_time)
    courses_list_page.click_del_course(index=0)