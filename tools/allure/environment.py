import platform
import sys

from config import settings

def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items]
    items.append(f'OS_INFO: {platform.system()}, {platform.release()}')
    items.append(f'PYTHON VERSION: {sys.version}')
    
    properties = "\n".join(items)
    
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)