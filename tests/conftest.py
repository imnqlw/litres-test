from selene import browser
import pytest
import os
from selenium import webdriver





@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.windows_width =  1920
    browser.config.windows_heights = 1080

    yield browser
    browser.quit()

