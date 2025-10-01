from playwright.sync_api import Playwright
from allure_commons.types import AttachmentType
from config import settings, Browser
import allure




def initialize_playwright_page(playwright: Playwright, 
                               test_name: str,
                               browser_type: Browser,
                               storage_state: str | None = None
                               ):
    
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state, 
        record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    yield page
    
    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()
    allure.attach.file(source=settings.tracing_dir.joinpath(f'{test_name}.zip'), name=f'tracing {test_name}', extension='zip')
    allure.attach.file(source=page.video.path(), name=f'video {test_name}', attachment_type=AttachmentType.WEBM)
    