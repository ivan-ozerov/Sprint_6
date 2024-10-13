import random
from selenium import webdriver

# URL-s

MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
ORDER_PAGE_URL = MAIN_PAGE_URL + 'order'

# тестовые данные
COLORS = {
    '1' : 'чёрный жемчуг',
    '2' : 'серая безысходность'
}
MONTHS = {
    '01' : 'января',
    '02' : 'февраля',
    '03' : 'марта',
    '04' : 'апреля',
    '05' : 'мая',
    '06' : 'июня',
    '07' : 'июля',
    '08' : 'августа',
    '09' : 'сентября',
    '10' : 'октября',
    '11' : 'ноября',
    '12' : 'декабря',
    }
USER_DATA = [
    { 
    'name' : "Ясос",
    "surname" : "Биб",
    "address" : "ул. Пушкина",
    "subway" : "Преображенская площадь",
    "phone" : "89213156432",
    'date' : '05.10.2024',
    'time_of_rent' : 'четверо суток',
    'colors' : ['2'],
    'comment' : 'ну как ты там брат, братишка? братюльник-братюнец'
    },
    { 
    'name' : "Сергей",
    "surname" : "Петров",
    "address" : "пр. Энергетиков",
    "subway" : "Домодедовская",
    "phone" : "01234567890",
    'date' : '24.03.2022',
    'time_of_rent' : 'сутки',
    'colors' : ['1'],
    'comment' : 'no comments'
}
]

# Functions

def create_webdriver():
    return webdriver.Firefox()

def array_with_random_numbers(num_of_webelements):
    my_list = list(range(0, num_of_webelements))
    random.shuffle(my_list)
    return my_list
 
def convert_months_from_num_to_text(date):   
    result_date = f"{date[:2]} {MONTHS[date[3:5]]}"
    if result_date[0] == '0':
        result_date = result_date[1:]
    return result_date

def convert_color_nums_to_colors(color_nums):
    if len(color_nums) == 0:
        return 'любой'
    else:
        return ', '.join([COLORS[color_num] for color_num in color_nums])
    
def return_all_data():
    all_data = {**CORRECT_USER_INFO, **SECOND_FORM_DATA}
    all_data['date'] = convert_months_from_num_to_text(all_data['date'])
    all_data['colors'] = convert_color_nums_to_colors(all_data['colors'])
    return all_data