import pytest
from selenium import webdriver
from locators.order_page_locators import OrderPageLocators
import helper
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.track_page import TrackPage
import time
from pprint import pprint

class TestTrackPage:

    driver = None

    @classmethod
    def test_setup_class(cls, driver):
        cls.driver = driver

    @pytest.mark.parametrize('user_data', helper.USER_DATA)
    def test_correct_data_in_status_window(self, user_data, open_main_page):
        main_page = MainPage(self.driver)
        order_page = OrderPage(main_page.go_to_order_page_from_header())
        track_page = TrackPage(*order_page.full_flow_from_order_page_to_track_page(user_data))
        all_elements_text = track_page.get_all_elements_text_in_track_info()
        assert user_data == all_elements_text
        