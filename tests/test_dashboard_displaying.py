from pages.dashboard_page import DashboardPage

def test_dashboard_displaying(dashboard_page_with_state: DashboardPage, ):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.navbar.check_visible('username')
    dashboard_page_with_state.check_page_title()
    dashboard_page_with_state.check_students_chart()
    dashboard_page_with_state.check_activities_chart()
    dashboard_page_with_state.check_courses_chart()
    dashboard_page_with_state.check_scores_chart()
    dashboard_page_with_state.side_bar.check_visible()