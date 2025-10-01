from pages.dashboard.dashboard_page import DashboardPage
import allure
import pytest
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from tools.routes import AppRoute


@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.toolbar.check_visible()
        dashboard_page_with_state.check_students_chart()
        dashboard_page_with_state.check_activities_chart()
        dashboard_page_with_state.check_courses_chart()
        dashboard_page_with_state.check_scores_chart()
        dashboard_page_with_state.side_bar.check_visible()