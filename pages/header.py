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
        self.driver = driver 
        self.link_to_ya_dzen = HeaderLocators.HEADER__LOGO_TO_YA_DZEN
        self.link_to_ya_samokat = HeaderLocators.HEADER__LOGO_TO_YA_SAMOKAT

    def click_on_link_to_ya_dzen(self):
        self.click(self.link_to_ya_dzen)


    def click_on_link_to_ya_samokat(self):
        self.click(self.link_to_ya_samokat)


    def wait_until_current_url_will_be_dzen(self):
        WebDriverWait(self.driver, 3).until(EC.url_contains, 'https://dzen.ru/')