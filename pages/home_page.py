import time

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step("Нажатие на элемент аккордеона и забираем ответ на вопрос")
    def get_accordion(self, locator_q, locator_t):
        # Нажимаем на элемент аккордеона и получаем его атрибут
        question_attribute = self.find_and_click_element(locator_q).get_attribute("aria-disabled")
        text_answer = self.get_text_element(locator_t)  # Получаем текст открытого элемента аккордеона
        return question_attribute, text_answer
