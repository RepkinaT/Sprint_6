from selenium.webdriver.common.by import By


class LocatorAccordion:
    # Выпадающий список
    ACCORDION_ITEM_1 = (By.ID, "accordion__heading-0")
    ACCORDION_ITEM_2 = (By.ID, "accordion__heading-1")
    ACCORDION_ITEM_3 = (By.ID, "accordion__heading-2")
    ACCORDION_ITEM_4 = (By.ID, "accordion__heading-3")
    ACCORDION_ITEM_5 = (By.ID, "accordion__heading-4")
    ACCORDION_ITEM_6 = (By.ID, "accordion__heading-5")
    ACCORDION_ITEM_7 = (By.ID, "accordion__heading-6")
    ACCORDION_ITEM_8 = (By.ID, "accordion__heading-7")

    # Текст выпадающего списка
    ACCORDION_TEXT_1 = (By.ID, "accordion__panel-0")
    ACCORDION_TEXT_2 = (By.ID, "accordion__panel-1")
    ACCORDION_TEXT_3 = (By.ID, "accordion__panel-2")
    ACCORDION_TEXT_4 = (By.ID, "accordion__panel-3")
    ACCORDION_TEXT_5 = (By.ID, "accordion__panel-4")
    ACCORDION_TEXT_6 = (By.ID, "accordion__panel-5")
    ACCORDION_TEXT_7 = (By.ID, "accordion__panel-6")
    ACCORDION_TEXT_8 = (By.ID, "accordion__panel-7")


class LocatorOrderButton:
    # Кнопка заказать в правом верхнем углу сайта
    BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[contains(text(), 'Заказать')]")
    # Кнопка заказать в центре на главной странице сайта
    BUTTON_CENTER = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[contains(text(), 'Заказать')]")

