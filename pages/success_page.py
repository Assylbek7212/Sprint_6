from selenium.webdriver.common.by import By
import allure
from helpers.base_page import BasePage
from helpers.constants import success_text
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckSuccessOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
        self.yes_button = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
        self.order = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")
        self.button_new_order = (
            By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

    @allure.step('Находим и нажимаем на кнопку заказать')
    def click_button_order(self):
        self.click_element(*self.button_order)

    @allure.step('Подтверждаем заказ и нажимаем на кнопку "да"')
    def confirm_order(self):
        element = self.driver.find_element(*self.yes_button)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверяем успешность формирования заказа')
    def check_success(self):
        text = self.get_element_text(self.yes_button)
        return text

    @allure.step('Находим и нажимаем на кнопку перехода сформировавшегося заказа')
    def check_click_view_order(self):
        self.click_element(self.button_new_order)

    @allure.step('Завершить заказ')
    def complete_order_process(self):
        self.click_button_order()
        self.check_success()
        self.confirm_order()

