import pytest

@pytest.mark.smoke
def test_smoke_case():
    assert True is True

@pytest.mark.regression
def test_regression_test():
    assert 2 + 2 == 4
    
@pytest.mark.smoke
class TestSuite:
    
    def test_case_1():
        assert 1 == 1
    
    
    def test_case_2():
        assert 2 != 3
        
@pytest.mark.regression
class TestUserAuthentication:
    
    @pytest.mark.smoke
    def test_login():
        assert True
    
    @pytest.mark.slow
    def test_password_reset():
        assert True
        
    def test_logout():
        assert True
    
@pytest.mark.critical
@pytest.mark.smoke    
@pytest.mark.regression
def test_critical_login():
    assert True
    
    
@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass