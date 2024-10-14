from selenium import webdriver
from selenium.webdriver.common.by import By

# Страница заказа
class OrderPageLocators:
    
    # первая форма
    # поле ввода имени
    ORDER_PAGE__NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    # поле ввода фамилии
    ORDER_PAGE__SURNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    # поле ввода адреса
    ORDER_PAGE__ADRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    # поле ввода станции метро
    ORDER_PAGE__SUBWAY_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    # поле ввода телефона
    ORDER_PAGE__PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    # кнопка "Далее"
    ORDER_PAGE__BUTTON_CONTINUE = (By.XPATH, '//button[text()="Далее"]')
    # форма
    ORDER_PAGE__FORM = (By.XPATH, '//div[starts-with(@class, "Order_Form")]')
    # раскрывающийся список станций метро
    ORDER_PAGE__SUBWAY_ELEMENT = (By.CLASS_NAME, 'div.select-search__row')
    # заголовок второй формы заказа
    ORDER_PAGE__HEADER = (By.XPATH, '//div[contains(@class,"Order_Header")]')
    # все элементы страницы заказа
    ORDER_PAGE__FIRST_FORM__ALL_ELEMENTS = {
        'name_input' : ORDER_PAGE__NAME_INPUT,
        'surname_input' : ORDER_PAGE__SURNAME_INPUT,
        'address_input' : ORDER_PAGE__ADRESS_INPUT,
        'subway_input' : ORDER_PAGE__SUBWAY_INPUT,
        'phone_input' : ORDER_PAGE__PHONE_INPUT,
        'continue_button' : ORDER_PAGE__BUTTON_CONTINUE,
        'order_form' : ORDER_PAGE__FORM,
        'subway_list' : ORDER_PAGE__SUBWAY_ELEMENT,
        'second_header' : ORDER_PAGE__HEADER
    }  

    @classmethod  
    def get_modified_locator(cls, type, value):
        if type == 'subway':
            return (By.XPATH, f'//div[@class="select-search__select"]//div[contains(text(), "{value}")]')
        elif type == 'rent_time':
            return (By.XPATH, f'//div[@class="Dropdown-menu"]/div[@class="Dropdown-option"][text()="{value}"]')
        elif type == 'color_num':
            return (By.XPATH, f'//label[contains(@class, "Checkbox_Label")][{value}]//input[@type="checkbox"]')

    # вторая форма
    # поле ввода даты
    ORDER_PAGE__DATE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    # поле ввода срока аренды
    ORDER_PAGE__RENT_TIME_FIELD = (By.XPATH, '//div[text()="* Срок аренды"]/parent::div/parent::div')
    # поле ввода срока аренды
    ORDER_PAGE__RENT_TIME_OPTION = (By.XPATH, 'div[class="Dropdown-menu"]/div[class="Dropdown-option"]')
    # поле ввода цвета самоката
    ORDER_PAGE__COLOR_CHECKBOXES = (By.XPATH, '//label[contains(@class, "Checkbox_Label"]//input[type="checkbox"]')
    # поле ввода комментария
    ORDER_PAGE__COMMENT_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    # кнопка "Заказать"
    ORDER_PAGE__ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')
    # все элементы 2й формы страницы Заказа
    ORDER_PAGE__SECOND_FORM__ALL_ELEMENTS = {
        'date_input' : ORDER_PAGE__DATE_INPUT,
        'rent_time_field' : ORDER_PAGE__RENT_TIME_FIELD,
        'rent_time_option' : ORDER_PAGE__RENT_TIME_OPTION,
        'color_checkboxes' : ORDER_PAGE__COLOR_CHECKBOXES,
        'comment_input' : ORDER_PAGE__COMMENT_INPUT,
        'order_button' : ORDER_PAGE__ORDER_BUTTON
    }

    # модалка подтверждения заказа
    # заголовок модалки 
    ORDER_PAGE__ORDER_CONFIRMATION_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")][text()="Хотите оформить заказ?"]')
    # кнопка "Да" в модалке
    ORDER_PAGE__ORDER_CONFIRMATION_BUTTON_ACCEPT = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Да"]')
    # все элементы модалки подтверждения заказа
    ORDER_PAGE__ORDER_CONFIRMATION_MODAL__ALL_ELEMENTS = {
        'modal_window_confirm_order__header' : ORDER_PAGE__ORDER_CONFIRMATION_HEADER,
        'modal_window_confirm_order__confirm_button' : ORDER_PAGE__ORDER_CONFIRMATION_BUTTON_ACCEPT
    }

    # модалка перехода на страницу статуса заказа
    # заголовок модалки
    ORDER_PAGE__ORDER_MODAL_COMPLETE_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]')
    # текст модалки
    ORDER_PAGE__ORDER_MODAL_COMPLETE_TEXT = (By.XPATH, '//div[contains(@class, "Order_Text")]')
    # кнопка Посмотреть статус
    ORDER_PAGE__ORDER_MODAL_WATCH_STATUS_BUTTON = (By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[text()="Посмотреть статус"]')
    # все элементы модалки перехода на страницу заказа
    ORDER_PAGE__ORDER_COMPLETE_MODAL__ALL_ELEMENTS = {
        'modal_window_complete_order__header' : ORDER_PAGE__ORDER_MODAL_COMPLETE_HEADER,
        'modal_window_complete_order__text' : ORDER_PAGE__ORDER_MODAL_COMPLETE_TEXT,
        'modal_window_complete_order__watch_status_button' : ORDER_PAGE__ORDER_MODAL_WATCH_STATUS_BUTTON
    }

    