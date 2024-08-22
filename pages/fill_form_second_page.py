from selenium.webdriver.common.by import By
from helpers.constants import *
import allure
from helpers.base_page import BasePage
from datetime import datetime, timedelta
import time
class FillFormSecond(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        self.time = (By.CLASS_NAME, "Dropdown-arrow")
        self.time_def = (By.XPATH, "//div[@class='Dropdown-option'][text()='двое суток']")
        self.color = (By.XPATH, "//input[@id='black']")
        self.comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")


    @allure.step('Находим поле даты доставки и выбираем дату')
    def fill_date(self):
        self.click_element(*self.date)
        self.send_keys(self.date, value=self.get_next_day())

    @allure.step('Выбрать следующий день календаря')
    def get_next_day(self):
        today = datetime.today()
        next_day = today + timedelta(days=1)
        formatted_next_day = next_day.strftime("%d.%m.%Y")
        return formatted_next_day

    @allure.step('Находим поле срока аренды и выбираем срок')
    def fill_time(self):
        self.click_element(*self.time)
        self.click_element(*self.time_def)

    @allure.step('Находим поле выбора цвета и выбираем цвет')
    def fill_color(self):
        self.click_element(*self.color)

    @allure.step('Находим поле комментария и вводим комментарий')
    def fill_comment(self, comment_text):
        self.send_keys(self.comment, comment_text)

    @allure.step("Заполняем форму заказа")
    def fill_form_order(self):
        self.fill_date()
        self.fill_time()
        self.fill_color()
        self.fill_comment(comment_form)
