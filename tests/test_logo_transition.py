import allure

from pages.order_page import OrderPage


class TestLogoTransition:
    @allure.story("TestLogoTransition")
    @allure.title("Тест перехода по лого Самокат")
    @allure.description(
        "Этот тест проверяет нажатие логотипа Самокат и переход на главную страницу сайта.")
    def test_logo_scooter(self, browser):
        order_page = OrderPage(browser)
        order_page.click_the_order_button()
        order_page.transition_logo_scooter()
        current_url = order_page.current_url()
        
        # Проверяем переход по логотипу на главную страницу сайта
        assert current_url == "https://qa-scooter.praktikum-services.ru/"
    
    @allure.story("TestLogoTransition")
    @allure.title("Тест перехода по лого Яндекс")
    @allure.description(
        "Этот тест проверяет нажатие логотипа Яндекс и открытие дополнительной вкладки браузера с сайтом Dzen.")
    def test_logo_yandex(self, browser):
        order_page = OrderPage(browser)
        order_page.transition_logo_yandex()
        expected_url = "https://dzen.ru/?yredirect=true"
        order_page.switch_to_last_tab(expected_url)
        current_url = order_page.current_url()
        
        # Проверяем переход по логотипу на другой сайт
        assert current_url == expected_url
