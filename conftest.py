import pytest
from selenium import webdriver
import helper


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(driver):
    driver.get(helper.MAIN_PAGE_URL)
