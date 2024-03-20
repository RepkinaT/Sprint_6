import allure

from locators.base_page_locators import LocatorLogo
from locators.home_page_locators import LocatorOrderButton
from locators.order_page_locators import LocatorRentalInformation1, LocatorRentalInformation2, \
    LocatorCompletingOrder
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажатие кнопки "Заказать"')
    def click_the_order_button(self, button=LocatorOrderButton.BUTTON_TOP):
        self.click_on_element(button)  # Нажимаем на кнопку

    @allure.step('Первый ввод данных о покупателе')
    def enter_customer_data(self, data):
        # Заполняем форму заказа (ФИО, адрес, номер телефона)
        for locator, value in [
            (LocatorRentalInformation1.NAME_INPUT, data.NAME),
            (LocatorRentalInformation1.SURNAME_INPUT, data.SURNAME),
            (LocatorRentalInformation1.ADDRESS_INPUT, data.ADDRESS),
            (LocatorRentalInformation1.TELEPHONE_INPUT, data.TELEPHONE),
        ]:
            self.find_element_send_keys(locator, value)

        # Заполняем форму заказа с выбором метро
        self.click_on_element(LocatorRentalInformation1.METRO_OPTIONS)
        self.click_on_element(LocatorRentalInformation1.METRO_STATION)

    @allure.step('Нажатие кнопки "Далее"')
    def click_the_next_button(self):
        self.click_on_element(LocatorRentalInformation1.SUBMIT_BUTTON)  # Нажимаем на кнопку

    @allure.step('Второй ввод данных о товаре и дате доставки')
    def enter_rental_data(self, data):
        # Заполняем вторую форму заказа (Дата, период, цвет самоката)
        for locator in [
            LocatorRentalInformation2.DATE_OPTIONS,
            LocatorRentalInformation2.DATE_CHOICE,
            LocatorRentalInformation2.PERIOD_OPTIONS,
            LocatorRentalInformation2.PERIOD_CHOICE,
            LocatorRentalInformation2.COLOR_CHOICE,
        ]:
            self.click_on_element(locator)

        # Заполняем комментарий
        self.find_element_send_keys(LocatorRentalInformation2.COMMENT_INPUT, data.COMMENT)

    @allure.step('Нажатие кнопки Заказать')
    def click_the_order(self):
        self.click_on_element(LocatorRentalInformation2.SUBMIT_BUTTON)  # Нажимаем на кнопку

    @allure.step('Нажатие кнопки "Да" для подтверждения оформления заказа')
    def placing_an_order(self):
        self.click_on_element(LocatorCompletingOrder.AGREE_BUTTON)  # Нажимаем на кнопку подтверждения заказа

    @allure.step('Получаем кнопку "Статус заказа"')
    def status_order(self):
        return self.get_text_element(LocatorCompletingOrder.WATCH_STATUS_BUTTON)  # Получаем текст кнопки

    @allure.step('Нажатие на лого "Самокат"')
    def transition_logo_scooter(self):
        self.click_the_order_button(LocatorLogo.SCOOTER_LOGO)  # Нажимаем на лого

    @allure.step('Нажатие на лого "Яндекс"')
    def transition_logo_yandex(self):
        self.click_the_order_button(LocatorLogo.YANDEX_LOGO)  # Нажимаем на лого

    @allure.step('Переходим на открывшееся кладку dzen')
    def switch_to_last_tab(self, expected_url):
        self.switch_to()  # Переходим на другую вкладку
        self.url_to_be(expected_url)  # Ожидаем когда страница на вкладке прогрузится
