from playwright.sync_api import Playwright
from allure_commons.types import AttachmentType
import allure




def initialize_playwright_page(playwright: Playwright, 
                               test_name: str,
                               storage_state: str | None = None
                               ):
    
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state=storage_state, record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    yield page
    
    context.tracing.stop(path=f'./tracing/{test_name}.zip')
    browser.close()
    allure.attach.file(source=f'./tracing/{test_name}.zip', name=f'tracing {test_name}', extension='zip')
    allure.attach.file(source=page.video.path(), name=f'video {test_name}', attachment_type=AttachmentType.WEBM)