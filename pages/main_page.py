from selenium import webdriver
from locators.main_page_locators import MainPageLocators
import helper
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
from random import random

class MainPage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver)
        self.FAQ_block = MainPageLocators.MAIN_PAGE__FAQ_CONTAINER
        self.FAQ_item = MainPageLocators.MAIN_PAGE__FAQ_ITEM
        self.FAQ_last_item = MainPageLocators.MAIN_PAGE__FAQ_LAST_ITEM
        self.FAQ_button = MainPageLocators.MAIN_PAGE__FAQ_BUTTON
        self.FAQ_panel = MainPageLocators.MAIN_PAGE__FAQ_PANEL
        self.order_button_in_header = MainPageLocators.MAIN_PAGE__ORDER_BUTTON__IN_HEADER
        self.order_button_at_bottom = MainPageLocators.MAIN_PAGE__ORDER_BUTTON__AT_THE_BOTTOM
        self.cookie_acception_button = MainPageLocators.MAIN_PAGE__COOKIE_BUTTON

    
    def get_cookie_button(self):
        return self.find(self.cookie_acception_button)
    
    def click_cookie_button(self):
        self.click(self.cookie_acception_button)
    
    def wait_until_cookie_button_is_not_displayed(self):
        return self.wait_unt_not(self.cookie_acception_button)

    # def wait_cookie_button_is_invisible(self):

    def get_FAQ_last_item(self):
        return self.find(self.FAQ_last_item)

    def get_FAQ_button(self, item_number):
        return (self.find_multiple(self.FAQ_button))[item_number]

    def get_FAQ_panel(self, item_number):
        return self.find_multiple(self.FAQ_panel)[item_number]

    def get_FAQ_block(self):
        return self.find(self.FAQ_block)

    def click_FAQ_button(self, item_number):
        elements = self.driver.find_elements(*self.FAQ_button)
        elements[item_number].click()

    def get_order_button_in_header(self):
        return self.find(self.order_button_in_header)
    
    def click_order_button_in_header(self):
        self.click(self.order_button_in_header)

    def get_order_button_at_bottom(self):
        return self.find(self.order_button_at_bottom)

    def click_order_button_at_bottom(self):
        self.click(self.order_button_at_bottom)

    def wait_until_element_is_visible(self, element_locator):
        self.wait(element_locator)
        
    def click_in_cookie_acception_button(self):
        self.click(self.cookie_acception_button)

    def go_to_order_page_from_header(self):
        self.scroll_to_element(self.get_order_button_in_header())
        self.wait(self.order_button_in_header)
        self.click_order_button_in_header()
        return self.driver

    def go_to_order_page_from_bottom(self):
        self.scroll_to_element(self.get_order_button_at_bottom())
        self.wait(self.order_button_at_bottom)
        self.click_order_button_at_bottom()
        

    