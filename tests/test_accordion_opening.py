import allure
import pytest

from data import Answers
from locators.base_page_locators import LocatorCookie
from locators.home_page_locators import LocatorAccordion
from pages.home_page import HomePage


class TestAccordionOpening:
    @pytest.mark.parametrize("locator_q, locator_t, answer", [
        (
                getattr(LocatorAccordion, f"ACCORDION_ITEM_{i}"),
                getattr(LocatorAccordion, f"ACCORDION_TEXT_{i}"),
                getattr(Answers, f"ANSWER_{i}")
        )
        for i in range(1, 9)
    ])
    @allure.story("TestAccordionOpening")
    @allure.title("Тест accordion opening")
    @allure.description(
        'Этот тест проверяет выпадающий список в разделе "Вопросы о важном"')
    def test_accordion_opening(self, browser, locator_q, locator_t, answer):
        home_page = HomePage(browser)
        home_page.accept_cookies(LocatorCookie.BUTTON)  # Принимаем куки
        question_attribute, text_answer = home_page.get_accordion(locator_q, locator_t)
        
        # Проверяем открытие элемента аккордеона, атрибут которого должен быть равен 'true' и
        # сверяем текст ответа с ответом из класса
        assert question_attribute == 'true' and text_answer == answer
