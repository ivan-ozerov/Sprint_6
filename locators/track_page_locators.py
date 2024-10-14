from selenium import webdriver
from selenium.webdriver.common.by import By

class TrackPageLocators:

    # страница со статусом заказа
    # блок с информацией о заказе
    TRACK_PAGE__ORDER_INFO_BLOCK = (By.XPATH, '//div[contains(@class, "Track_OrderInfo")]')
    # информация в заказе об имени
    TRACK_PAGE__TRACK_NAME_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Имя")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе о фамилии
    TRACK_PAGE__TRACK_SURNAME_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Фамилия")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе об адресе
    TRACK_PAGE__TRACK_ADDRESS_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Адрес")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе о станции метро
    TRACK_PAGE__TRACK_SUBWAY_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Станция метро")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе о телефоне
    TRACK_PAGE__TRACK_PHONE_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Телефон")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе о дате
    TRACK_PAGE__TRACK_DATE_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Дата доставки")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе о периоде аренды
    TRACK_PAGE__TRACK_RENT_TIME_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Срок аренды")]/following-sibling::div[contains(@class, "Track_Value")]')
    # информация в заказе о цветах самокатов
    TRACK_PAGE__TRACK_COLOR_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Цвет")]/following-sibling::div[contains(@class, "Track_Value")]')
    # комментарий
    TRACK_PAGE__TRACK_COMMENT_VALUE = (By.XPATH, '//div[contains(@class, "Track_Title") and contains(text(), "Комментарий")]/following-sibling::div[contains(@class, "Track_Value")]')
    # все элементы страницы Статуса заказа
    TRACK_PAGE__ALL_ELEMENTS = {
        'name' : TRACK_PAGE__TRACK_NAME_VALUE,
        'surname' : TRACK_PAGE__TRACK_SURNAME_VALUE,
        'address' : TRACK_PAGE__TRACK_ADDRESS_VALUE,
        'subway' : TRACK_PAGE__TRACK_SUBWAY_VALUE,
        'phone' : TRACK_PAGE__TRACK_PHONE_VALUE,
        'date' : TRACK_PAGE__TRACK_DATE_VALUE,
        'time_of_rent' : TRACK_PAGE__TRACK_RENT_TIME_VALUE,
        'colors' : TRACK_PAGE__TRACK_COLOR_VALUE,
        'comment' : TRACK_PAGE__TRACK_COMMENT_VALUE
    }