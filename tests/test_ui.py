# tests/test_ui.py
import os
from selenium import webdriver

def test_lambdatest_run():
    lt_username = os.getenv("LT_USERNAME")
    lt_access_key = os.getenv("LT_ACCESS_KEY")

    capabilities = {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "LT:Options": {
            "platformName": "Windows 10",
            "build": "CircleCI Build",
            "name": "LambdaTest Sample Test",
            "selenium_version": "4.0.0"
        }
    }

    remote_url = f"https://{lt_username}:{lt_access_key}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)

    try:
        driver.get("https://example.com")
        assert "Example Domain" in driver.title
    finally:
        driver.quit()
