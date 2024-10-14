from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import helper
from pages.header import Header
import random
import pytest
import time

class TestHeader:
    
    driver = None

    @classmethod
    def test_setup_class(cls, driver: WebDriver):
        cls.driver = driver

    def test_open_ya_samokat(self, open_main_page: None):
        header = Header(self.driver)
        header.click_on_link_to_ya_samokat()
        assert header.driver.current_url == helper.MAIN_PAGE_URL

    def test_open_ya_dzen(self, open_main_page: None):
        header = Header(self.driver)
        header.click_on_link_to_ya_dzen()
        header.switch_to_last_tab()
        header.wait(header.dzen_search_form)
        assert 'Поиск Яндекса' in header.find(header.dzen_search_form).get_attribute('data-params')
        