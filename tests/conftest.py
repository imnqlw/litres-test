from selene import browser
import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from utils import attach

# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
# DEFAULT_BROWSER_VERSION = "100.0"
#
# selenoid_login = os.getenv('SELENOID_LOGIN')
# selenoid_pass = os.getenv('SELENOID_PASS')


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    # browser_version = DEFAULT_BROWSER_VERSION
    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": browser_version,
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(
    #     command_executor=f"https://{selenoid_login}:{selenoid_pass}@selenoid.autotests.cloud/wd/hub",
    #     options=options)
    #
    #browser = Browser(Config(driver))


    browser.config.base_url = 'https://www.litres.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    yield browser

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()
