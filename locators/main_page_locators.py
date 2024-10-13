from selenium import webdriver
from selenium.webdriver.common.by import By

# Главная страница
class MainPageLocators:
    # контейнер для FAQ
    MAIN_PAGE__FAQ_CONTAINER = (By.XPATH, '//div[contains(class, Home_FAQ)]')
    # компонент FAQ конетйнера
    MAIN_PAGE__FAQ_ITEM = (By.XPATH, '//div[contains(class, Home_FAQ)]//div[@class="accordion__item"]')
    # компонент FAQ конетйнера
    MAIN_PAGE__FAQ_LAST_ITEM = (By.XPATH, '//div[contains(class, Home_FAQ)]//div[@class="accordion__item"][last()]')
    # кнопка компонента FAQ конетйнера
    MAIN_PAGE__FAQ_BUTTON = (By.XPATH, '//div[contains(class, Home_FAQ)]//div[@class="accordion__button"]')
    # содержание компонента FAQ конетйнера
    MAIN_PAGE__FAQ_PANEL = (By.XPATH, '//div[contains(class, Home_FAQ)]//div[@class="accordion__panel"]')
    # кнопка "Заказать" в хэдере
    MAIN_PAGE__ORDER_BUTTON__IN_HEADER = (By.XPATH, '//div[starts-with(@class, "Header")]//button[text()="Заказать"]')
    # кнопка "Заказать" внизу страницы
    MAIN_PAGE__ORDER_BUTTON__AT_THE_BOTTOM = (By.XPATH, '//div[starts-with(@class, "Home_FinishButton")]//button[text()="Заказать"]')
    # кнопка "Да все привыкли" 
    MAIN_PAGE__COOKIE_BUTTON = (By.XPATH, '//button[contains(@class, "App_CookieButton")]')



