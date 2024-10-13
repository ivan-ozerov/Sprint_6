from selenium import webdriver
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
    def setup_class(cls):
        cls.driver = helper.create_webdriver()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(1)

    @classmethod
    def setup_method(cls):
        cls.driver.get(helper.MAIN_PAGE_URL)

    def test_open_ya_samokat(self):
        header = Header(self.driver)
        header.click_on_link_to_ya_samokat()
        assert header.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_open_ya_dzen(self):
        header = Header(self.driver)
        ya_samokat_tab = header.driver.current_window_handle
        header.click_on_link_to_ya_dzen()
        opened_tabs = header.driver.window_handles
        window_url = header.driver.current_url
        for tab in opened_tabs:
            if tab!=ya_samokat_tab:
                header.driver.switch_to.window(tab)
                header.wait_until_current_url_will_be_dzen()
                time.sleep(2)
                window_url = header.driver.current_url
        assert "https://dzen.ru/" in window_url
        print(opened_tabs)
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()