from selenium import webdriver
from locators.order_page_locators import OrderPageLocators
import helper
from pages.main_page import MainPage
from pages.order_page import OrderPage
import time
import pytest
from pprint import pprint

class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = helper.create_webdriver()
        cls.driver.maximize_window()

    @classmethod
    def setup_method(cls):
        cls.driver.get(helper.MAIN_PAGE_URL)

    # @classmethod
    # def setup_method(cls):
    #     cls.driver.get(helper.ORDER_PAGE_URL)

    def test_correct_user_data_and_click_open_second_form(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(main_page.go_to_order_page_from_header())
        order_page.fill_in_first_form_and_click_continue(helper.USER_DATA[0])
        assert order_page.get_second_form_header_text() == "Про аренду"

    def test_correct_rent_data_and_click_open_confirm_window(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(main_page.go_to_order_page_from_header())
        order_page.fill_in_first_form_and_click_continue(helper.USER_DATA[0])
        order_page.fill_in_second_form_and_make_order(helper.USER_DATA[0])
        assert order_page.get_header_in_order_modal_window() == 'Хотите оформить заказ?'

    def test_complete_order_window_open(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(main_page.go_to_order_page_from_header())
        order_page.fill_in_first_form_and_click_continue(helper.USER_DATA[0])
        order_page.fill_in_second_form_and_make_order(helper.USER_DATA[0])
        order_page.click_order_confirm_button()
        assert 'Заказ оформлен' in order_page.get_header_in_order_complete_modal_window()

    @pytest.mark.parametrize('user_data', helper.USER_DATA)
    def test_watch_order_status_window_open(self, user_data):
        main_page = MainPage(self.driver)
        order_page = OrderPage(main_page.go_to_order_page_from_header())
        driver_and_ord_number = order_page.full_flow_from_order_page_to_track_page(user_data)
        assert order_page.driver.current_url == f'https://qa-scooter.praktikum-services.ru/track?t={driver_and_ord_number[1]}'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    