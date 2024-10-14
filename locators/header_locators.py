from selenium import webdriver
from selenium.webdriver.common.by import By


class HeaderLocators:

    # ссылка на яндекс-дзен
    HEADER__LOGO_TO_YA_DZEN = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")][@href="//yandex.ru"]')
    # ссылка на яндекс самокат
    HEADER__LOGO_TO_YA_SAMOKAT = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")][@href="/"]')
    # лого Яндекс Дзена
    YANDEX_DZEN_SEARCH_FORM = (By.XPATH, "//form[contains(@action, 'https://yandex.ru/search/')]")
