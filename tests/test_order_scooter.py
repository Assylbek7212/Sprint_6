from pages.fill_form_first_page import FillFormFirst
from pages.fill_form_second_page import FillFormSecond
from pages.order_scooter_button_main_page import OrderScooterButton
from pages.success_page import CheckSuccessOrder
from helpers.constants import *
from helpers.helpers import *
import allure
import pytest

class TestOrderScooter:
    @pytest.mark.parametrize("button_order", [
        OrderPageLocators.BUTTON_ORDER_TOP,
        OrderPageLocators.BUTTON_ORDER_BOTTOM
    ])
    @allure.description(
        'Заказ самоката. Проверяем весь флоу позитивного сценария')
    @allure.title("Заказ самоката")
    def test_order_scooter_up(self, driver, button_order):
        main_page = OrderScooterButton(driver)
        main_page.go_to_url_main(url)
        main_page.click_button(button_order)

        form_page1 = FillFormFirst(driver)
        form_page1.fill_form_and_click_button()

        form_page2 = FillFormSecond(driver)
        form_page2.fill_form_order()

        check_page = CheckSuccessOrder(driver)
        check_page.complete_order_process()
