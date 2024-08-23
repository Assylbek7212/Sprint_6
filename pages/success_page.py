from selenium.webdriver.common.by import By
import allure
from helpers.base_page import BasePage


class CheckSuccessOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
        self.button_confirm = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
        self.order = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and contains(text(), "
                                "'Заказ оформлен')]")
        self.button_cancel_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM "
                                              "Button_Inverted__3IF-i' and text()='Отменить заказ']")
        self.button_new_order = (
            By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

    @allure.step('Находим и нажимаем на кнопку заказать')
    def click_button_order(self):
        self.click_element(*self.button_order)

    @allure.step('Подтверждаем заказ и нажимаем на кнопку "да"')
    def confirm_order(self):
        self.click_element(*self.button_confirm)

    @allure.step('Проверяем успешность формирования заказа')
    def check_success(self):
        self.find_element(*self.order)

    @allure.step('Находим и нажимаем на кнопку перехода сформировавшегося заказа')
    def check_click_view_order(self):
        self.click_element(*self.button_new_order)

    @allure.step('Находим и нажимаем на кнопку перехода сформировавшегося заказа')
    def check_click_view_order(self):
        self.click_element(*self.button_new_order)

    @allure.step('Проверка наличия кнопки "Отменить заказ"')
    def check_cancel_order_button(self):
        self.find_element(*self.button_cancel_order)

    @allure.step('Проверка успешности формирования заказа')
    def complete_order_process(self):
        self.click_button_order()
        self.confirm_order()
        self.check_success()
        self.check_click_view_order()
        self.check_cancel_order_button()
