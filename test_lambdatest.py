import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # 1. LambdaTest credentials
    LT_USERNAME = os.getenv("LT_USERNAME")
    LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

    # 2. LambdaTest capabilities
    lt_options = {
        "platformName": "Windows 10",
        "build": "CircleCI Build",
        "name": "LambdaTest Secure Test",
        "selenium_version": "4.0.0",
        "w3c": True
    }

    chrome_options = Options()
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("browserVersion", "latest")
    chrome_options.set_capability("LT:Options", lt_options)

    # 3. Initialize remote driver (without service parameter)
    driver = webdriver.Remote(
        command_executor=f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub",
        options=chrome_options
    )
    
    yield driver
    driver.quit()

def test_lambdatest_run(driver):
    """Verify page title on LambdaTest"""
    driver.get("https://example.com")
    assert "Example" in driver.title


