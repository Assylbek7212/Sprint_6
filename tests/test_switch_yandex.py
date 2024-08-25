from pages.click_logo_yandex import CheckLogoYandex
import allure


class TestSwitchScooter:
    @allure.description(
        'Осуществляет проверку перехода при нажатии на лого Яндекса')
    @allure.title('Переход по лого "Яндекс"')
    def test_switch_scooter(self, driver):
        order_page_logo_yandex = CheckLogoYandex(driver)
        order_page_logo_yandex.check_click_logo_yandex()
