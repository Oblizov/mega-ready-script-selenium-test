import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.browser_version = '125.0'
    options.add_argument('hide-scrollbars')
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False,
        "goog:chromeOptions": {
            "args": ["--start-fullscreen"]}
    })

    selenium_grid_url = "http://localhost:4444/wd/hub"

    driver = webdriver.Remote(
        command_executor=selenium_grid_url,
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()