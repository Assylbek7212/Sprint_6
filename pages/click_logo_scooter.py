from selenium.webdriver.common.by import By
import allure
from helpers.constants import *
from helpers.base_page import BasePage
from pages.order_scooter_button_main_page import OrderScooterButton


class CheckLogoScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
        self.button_order1 = (By.XPATH, "//button[@class='Button_Button__ra12g']")

    @allure.step('Проверяем путь при нажатии на лого "Самокат"')
    def check_click_logo_scooter(self):
        self.go_to_url(url)
        self.click_element(*self.button_order1)
        current_url = self.get_current_url()
        self.click_element(*self.logo_scooter)
        self.wait_for_url_change(current_url)
        new_url = self.get_current_url()
        assert new_url == url, f"URL после перехода не соответствует ожидаемому: {new_url}"

