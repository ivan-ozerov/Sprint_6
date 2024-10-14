from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import helper
from pages.main_page import MainPage
import random
import pytest

class TestMainPage:

    driver = None

    @classmethod
    def test_setup_class(cls, driver):
        cls.driver = driver

    def test_order_page_opens_after_click_order_button_in_header(self, open_main_page):
        main_page = MainPage(self.driver)
        main_page.go_to_order_page_from_header()
        assert main_page.driver.current_url == helper.ORDER_PAGE_URL

    def test_order_page_opens_after_click_order_button_at_bottom(self, open_main_page):
        main_page = MainPage(self.driver)
        main_page.go_to_order_page_from_bottom()
        assert main_page.driver.current_url == helper.ORDER_PAGE_URL

    def test_check_cookie_button_is_not_displayed_after_click(self, open_main_page):
        # self.driver.get(helper.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        cookie_btn = main_page.get_cookie_button()
        cookie_btn.click()
        main_page.wait_until_cookie_button_is_not_displayed()

    @pytest.mark.parametrize('item_number', helper.array_with_random_numbers(7))
    def test_check_every_item_in_FAQ_block(self, item_number, open_main_page):
        main_page = MainPage(self.driver)
        main_page.click_FAQ_button(item_number)
        main_page.scroll_to_element(main_page.get_FAQ_last_item())
        main_page.wait_until_element_is_visible(main_page.FAQ_last_item)
        assert [main_page.get_FAQ_button(item_number).text, main_page.get_FAQ_panel(item_number).text] == helper.FAQ_SECTIONS_TEXT[item_number]
