from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helper

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, element_locator):
        return self.driver.find_element(*element_locator)

    def find_multiple(self,element_locator):
        return self.driver.find_elements(*element_locator)

    def wait(self, element_locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(element_locator))

    def wait_unt_not(self, element_locator):
        return WebDriverWait(self.driver, 3).until_not(EC.visibility_of_element_located(element_locator))

    def click(self, element_locator):
        self.find(element_locator).click()
    
    def get_text_of(self, element_locator):
        return self.find(element_locator).text

    def set_text_of(self, element_locator, text):
        self.find(element_locator).send_keys(text)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
