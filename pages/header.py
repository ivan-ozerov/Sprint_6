from selenium import webdriver
from locators.header_locators import HeaderLocators
import helper
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
from random import random
from pages.base_page import BasePage

class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 3)
        self.driver = driver 
        self.link_to_ya_dzen = HeaderLocators.HEADER__LOGO_TO_YA_DZEN
        self.link_to_ya_samokat = HeaderLocators.HEADER__LOGO_TO_YA_SAMOKAT
        self.dzen_search_form = HeaderLocators.YANDEX_DZEN_SEARCH_FORM

    def click_on_link_to_ya_dzen(self):
        self.click(self.link_to_ya_dzen)


    def click_on_link_to_ya_samokat(self):
        self.click(self.link_to_ya_samokat)


    def wait_ya_dzen_form_to_be_loaded(self):
        return self.wait(self.dzen_search_form)