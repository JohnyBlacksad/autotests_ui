import pytest

@pytest.fixture(autouse=True)
def send_analitycs_data():
    print('AUTOUSE: Отправляем аналитику')
    
@pytest.fixture(scope='session')
def settings():
    print('session: инициализируем настройки автотестов')
    
@pytest.fixture(scope='class')
def user():
    print('CLASS: Создаем данные пользователя один раз на тестовый класс')
    
    
@pytest.fixture(scope='function')
def browser():
    print('FUNCTION: Открываем браузер на каждый автотест')
    
    
class TestUserFlow:
    def test_user_can_login(self, settings):
        ...
        
    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...