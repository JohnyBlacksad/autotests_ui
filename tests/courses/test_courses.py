from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list import CoursesListPage
import pytest
import re


@pytest.mark.course
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_empty_result()
        courses_list_page.navbar.check_visible('username')
        courses_list_page.navbar.check_current_url(re.compile(r'.*/#/courses'))
        courses_list_page.side_bar.check_visible()
        

    @pytest.mark.parametrize('course_title, course_time, course_descr, course_max_score, course_min_score, course_task_title, course_task_descr', 
                            [('Playwright', '2 weeks', 'Playwright', '100', '10', 'Task 1', 'This is task 1')])
    def test_create_course(self, created_courses_page: CreateCoursePage, 
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
        
        created_courses_page.toolbar.check_visible(is_form_fill=False)
        created_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
        created_courses_page.course_form.check_visible()
        created_courses_page.check_empty_task_list()
        created_courses_page.image_upload_widget.upload_course_img(file='./testdata/files/image.jpg')
        created_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
        
        created_courses_page.course_form.fill(title=course_title,
                                            estimated_time=course_time,
                                            description=course_descr,
                                            max_score=course_max_score,
                                            min_score=course_min_score)
        
        created_courses_page.exercises_toolbar.click_add_exercise_button()
        
        created_courses_page.course_exercise_form.fill(title=course_task_title,
                                                description=course_task_descr,
                                                index=0)
        
        created_courses_page.course_exercise_form.check_visible(index=0, 
                                                                title=course_task_title, 
                                                                description=course_task_descr)
        
        created_courses_page.toolbar.check_visible(is_form_fill=True)
        
        created_courses_page.toolbar.click_create_button()
        
        courses_list_page.course_view.check_visible(index=0, 
                                                    title=course_title,
                                                    max_score=course_max_score,
                                                    min_score=course_min_score,
                                                    estimated_time=course_time)
        
        courses_list_page.course_view.cart_menu.cilck_delete(index=0)
    
    def test_edit_course(self, created_courses_page: CreateCoursePage,  courses_list_page: CoursesListPage):
       
        created_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        created_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
        created_courses_page.course_form.check_visible()
        created_courses_page.check_empty_task_list()
        created_courses_page.image_upload_widget.upload_course_img(file='./testdata/files/image.jpg')
        created_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
        
        created_courses_page.course_form.fill(
            title='Title', estimated_time='4 weeks', description='Course description',
            max_score='100', min_score='10'
        )
        
        created_courses_page.exercises_toolbar.click_add_exercise_button()
        
        created_courses_page.course_exercise_form.fill(
            title='Task 1', description='Task 1 descr', index=0)
        
        created_courses_page.course_exercise_form.check_visible(index=0, title='Task 1', description='Task 1 descr')
        
        created_courses_page.toolbar.check_visible(is_form_fill=True)
        
        created_courses_page.toolbar.click_create_button()
        
        courses_list_page.course_view.check_visible(
            index=0, title='Title',estimated_time='4 weeks',
            max_score='100', min_score='10')
        
        courses_list_page.click_edit_course(index=0)
        
        created_courses_page.course_form.fill(
            title='Edit title', estimated_time='2 weeks', 
            description='Description', max_score='10', min_score='1')
        
        created_courses_page.toolbar.check_visible(is_form_fill=True)
        
        created_courses_page.toolbar.click_create_button()
        
        courses_list_page.course_view.check_visible(index=0,
            title='Edit title', estimated_time='2 weeks', 
            max_score='10', min_score='1')