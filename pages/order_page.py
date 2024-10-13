from selenium import webdriver
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import helper
import time
from random import random

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # элементы первой формы страницы Заказа
        self.order__first_form__all_elements = OrderPageLocators.ORDER_PAGE__FIRST_FORM__ALL_ELEMENTS
        # элементы второй формы страницы Заказа
        self.order__second_form__all_elements = OrderPageLocators.ORDER_PAGE__SECOND_FORM__ALL_ELEMENTS
        # элементы модального окна подтверждения заказа
        self.order__modal_window_confirm_order__all_elements = OrderPageLocators.ORDER_PAGE__ORDER_CONFIRMATION_MODAL__ALL_ELEMENTS
        # элементы модального окна подтвержденного заказа
        self.order__modal_window_complete_order__all_elements = OrderPageLocators.ORDER_PAGE__ORDER_COMPLETE_MODAL__ALL_ELEMENTS

    def get_second_form_header_text(self):
        return self.get_text_of(self.order__first_form__all_elements['second_header'])

    def fill_in_name_input(self, name):
        self.set_text_of(self.order__first_form__all_elements['name_input'], name)

    def fill_in_surname_input(self, surname):
        self.set_text_of(self.order__first_form__all_elements['surname_input'], surname)

    def fill_in_address_input(self, address):
        self.set_text_of(self.order__first_form__all_elements['address_input'], address)

    def fill_in_subway_input(self, subway):
        subway_element_locator = (By.XPATH, f'//div[@class="select-search__select"]//div[contains(text(), "{subway}")]')
        self.click(self.order__first_form__all_elements['subway_input'])
        self.set_text_of(self.order__first_form__all_elements['subway_input'], subway)
        self.wait(subway_element_locator)
        self.click(subway_element_locator)


    def fill_in_phone_input(self, phone):
        self.set_text_of(self.order__first_form__all_elements['phone_input'], phone)

    def click_continue_button(self):
        self.click(self.order__first_form__all_elements['continue_button'])

    def fill_in_first_form_and_click_continue(self, user_info):
        self.wait(self.order__first_form__all_elements['order_form'])
        self.fill_in_name_input(user_info['name'])
        self.fill_in_surname_input(user_info['surname'])
        self.fill_in_address_input(user_info['address'])
        self.fill_in_subway_input(user_info['subway'])
        self.fill_in_phone_input(user_info['phone'])
        self.click_continue_button()

    def fill_in_date_input(self, date):
        self.set_text_of(self.order__second_form__all_elements['date_input'], date)
        self.set_text_of(self.order__second_form__all_elements['date_input'], Keys.ESCAPE)
        

    def fill_in_rent_time_input(self, rent_time):
        self.click(self.order__second_form__all_elements['rent_time_field'])
        self.click((By.XPATH, f'//div[@class="Dropdown-menu"]/div[@class="Dropdown-option"][text()="{rent_time}"]'))

    def fill_in_color_checkbox(self, color_nums):
        for color_num in color_nums:
            self.click((By.XPATH, f'//label[contains(@class, "Checkbox_Label")][{color_num}]//input[@type="checkbox"]'))

    def fill_in_comment(self, comment):
        self.set_text_of(self.order__second_form__all_elements['comment_input'], comment)

    def click_order_button(self):
        self.click(self.order__second_form__all_elements['order_button'])

    def fill_in_second_form_and_make_order(self, user_data):
        self.fill_in_date_input(user_data['date'])
        self.fill_in_rent_time_input(user_data['time_of_rent'])
        self.fill_in_color_checkbox(user_data['colors'])
        self.fill_in_comment(user_data['comment'])
        self.click_order_button()

    def get_header_in_order_modal_window(self):
        return self.get_text_of(self.order__modal_window_confirm_order__all_elements['modal_window_confirm_order__header']).strip()
    
    def click_order_confirm_button(self):
        self.click(self.order__modal_window_confirm_order__all_elements['modal_window_confirm_order__confirm_button'])

    def get_header_in_order_complete_modal_window(self):
        return self.get_text_of(self.order__modal_window_complete_order__all_elements['modal_window_complete_order__header']).strip()
    
    def get_order_number(self):
        order_complete_window_text = self.get_text_of(self.order__modal_window_complete_order__all_elements['modal_window_complete_order__text'])
        substr_indexes = [len("Номер заказа: "), order_complete_window_text.find(".")]
        order_number = order_complete_window_text[substr_indexes[0]:substr_indexes[1]]
        return order_number

    def click_order_watch_status_button(self):
        self.click(self.order__modal_window_complete_order__all_elements['modal_window_complete_order__watch_status_button'])

    def full_flow_from_order_page_to_track_page(self, user_data):
        self.fill_in_first_form_and_click_continue(user_data)
        self.fill_in_second_form_and_make_order(user_data)
        self.click_order_confirm_button()
        order_number = self.get_order_number()
        self.click_order_watch_status_button()
        return self.driver, order_number

        