from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list import CoursesListPage
import pytest
import allure
import re
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from tools.routes import AppRoute


@pytest.mark.course
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_empty_result()
        courses_list_page.navbar.check_visible('username')
        courses_list_page.navbar.check_current_url(re.compile(r'.*/#/courses'))
        courses_list_page.side_bar.check_visible()
        

    @pytest.mark.parametrize('course_title, course_time, course_descr, course_max_score, course_min_score, course_task_title, course_task_descr', 
                            [('Playwright', '2 weeks', 'Playwright', '100', '10', 'Task 1', 'This is task 1')])
    @allure.title('Create with course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, created_courses_page: CreateCoursePage, 
                        courses_list_page: CoursesListPage,
                        course_title: str, 
                        course_time: str, 
                        course_descr: str,
                        course_max_score: int,
                        course_min_score: int,
                        course_task_title: str,
                        course_task_descr: str):
        
        courses_list_page.visit(AppRoute.COURSES)
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
    
    @allure.title('Create and edit created course')
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, created_courses_page: CreateCoursePage,  courses_list_page: CoursesListPage):
       
        created_courses_page.visit(AppRoute.COURSES_CREATE)
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