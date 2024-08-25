from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class OrderScooterButton(BasePage):

    BUTTON_ORDER_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, "
                                     "'Button_Middle__1CSJM')]")
    def __init__(self, driver):
        super().__init__(driver)
        self.button_order1 = (By.XPATH, "//button[@class='Button_Button__ra12g']")
        self.button_order2 = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and "
                                        "contains(@class, 'Button_Middle__1CSJM')]")
        self.open_button = (By.ID, "rcc-confirm-button")

    @allure.step('Переходим на сайт')
    def go_to_url_main(self, url):
        self.go_to_url(url)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button(self, button_order):
        self.click_element(*self.open_button)
        self.wait_until(button_order)
        self.click_element(*button_order)
