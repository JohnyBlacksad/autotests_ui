from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from tools.routes import AppRoute



@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.parametrize('email, username, password', 
                         [('test.name@gmail.com', 'testername', 'password')])
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_succesful_registration(self, registration_page: RegistrationPage,
                                    dashboard_page: DashboardPage, 
                                    email: str, 
                                    username: str, 
                                    password: str) -> None:
        
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.check_title()
        
        registration_page.fill_registration_form(email=email, 
                                                username=username, 
                                                password=password)
        
        registration_page.click_reg_button()
        dashboard_page.toolbar.check_visible()