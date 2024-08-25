from pages.click_logo_scooter import CheckLogoScooter
import allure


class TestSwitchScooter:
    @allure.description(
        'Осуществляет проверку перехода при нажатии на лого самоката')
    @allure.title('Переход по лого "Самокат"')
    def test_switch_scooter(self, driver):
        order_page_logo_scooter = CheckLogoScooter(driver)
        order_page_logo_scooter.check_click_logo_scooter()
