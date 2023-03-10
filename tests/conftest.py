import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield
    browser.quit()
