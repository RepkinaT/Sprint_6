import allure
import pytest

from data import DataOne, DataTwo
from locators.base_page_locators import LocatorCookie
from locators.home_page_locators import LocatorOrderButton
from pages.order_page import OrderPage


class TestOrderAScooter:
    @pytest.mark.parametrize("locator_button, data", {
        (LocatorOrderButton.BUTTON_TOP, DataOne),
        (LocatorOrderButton.BUTTON_CENTER, DataTwo),
    })
    @allure.story("TestOrderAScooter")
    @allure.title("Тест order a scooter (data: {data})")
    @allure.description(
        "Этот тест проверяет позитивный сценарий заказа самоката с двумя наборами данных и двумя точками входа.")
    def test_order_a_scooter(self, browser, locator_button, data):
        order_page = OrderPage(browser)
        order_page.accept_cookies(LocatorCookie.BUTTON)  # Принимаем куки
        order_page.click_the_order_button(locator_button)
        order_page.enter_customer_data(data)
        order_page.click_the_next_button()
        order_page.enter_rental_data(data)
        order_page.click_the_order()
        order_page.placing_an_order()
        status = order_page.status_order()
        
        # Проверяем успешное оформление заказа status должен быть равен "Посмотреть статус"
        assert status == "Посмотреть статус"
