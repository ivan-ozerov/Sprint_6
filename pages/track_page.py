from selenium import webdriver
from locators.track_page_locators import TrackPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import helper
import time
from random import random
from pages.order_page import OrderPage
from pages.base_page import BasePage


class TrackPage(BasePage):

    def __init__(self, driver, track_number=None):
        super().__init__(driver)
        self.track_page_info_block = TrackPageLocators.TRACK_PAGE__ORDER_INFO_BLOCK
        self.track_page_elements__all_elements = TrackPageLocators.TRACK_PAGE__ALL_ELEMENTS
        self.track_number = track_number


    def get_all_elements_text_in_track_info(self):
        all_elements_text = {}
        for element_name, element_locator in self.track_page_elements__all_elements.items():
            all_elements_text[element_name] = self.get_text_of(element_locator)
        return all_elements_text