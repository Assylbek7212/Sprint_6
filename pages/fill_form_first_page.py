import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers.constants import *
import allure
from helpers.base_page import BasePage


class FillFormFirst(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = (By.XPATH, "//input[@placeholder='* Имя']")
        self.lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
        self.address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        self.stmetro = (By.XPATH, "//input[@placeholder='* Станция метро']")
        self.number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        self.button_dalee = (By.XPATH, "//button[text()='Далее']")
        self.metro_station_name = (By.XPATH, f"//div[text()='{generate_random_stmetro()}']")

    @allure.step('Находим поле для ввода имени и вводим имя')
    def fill_name(self):
        self.send_keys(self.name, value=name_form)


    @allure.step('Находим поле для ввода фамилии и вводим фамилию')
    def fill_lastname(self):
        self.send_keys(self.lastname, value=lastname_form)

    @allure.step('Находим поле для ввода адреса и вводим адрес')
    def fill_address(self):
        self.send_keys(self.address, value=address_form)

    @allure.step('Находим поле для выбора метро и выбираем станцию')
    def fill_stmetro(self):
        self.click_element(*self.stmetro)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.metro_station_name)
        )
        self.click_element(*self.metro_station_name)

    @allure.step('Находим поле для ввода номера телефона и вводим номер телефона')
    def fill_number(self):
        self.send_keys(self.number, value=number_form)

    @allure.step('Находим кнопку "далее" и нажимаем на нее')
    def click_button(self):
        self.click_element(*self.button_dalee)

    @allure.step('Заполнение формы')
    def fill_form_and_click_button(self):
        self.fill_name()
        self.fill_lastname()
        self.fill_address()
        self.fill_stmetro()
        self.fill_number()
        self.click_button()
