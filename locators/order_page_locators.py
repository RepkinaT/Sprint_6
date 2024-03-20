from selenium.webdriver.common.by import By


class LocatorRentalInformation1:
    # Поля для заполнения первой формы
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_OPTIONS = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    METRO_STATION = (By.XPATH, ".//*[@class='select-search__row']")
    TELEPHONE_INPUT = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    # Кнопка Далее в первой форме
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")


class LocatorRentalInformation2:
    # Поля для заполнения второй формы
    DATE_OPTIONS = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    DATE_CHOICE = (By.XPATH, "//div[@aria-label = 'Choose суббота, 30-е марта 2024 г.']")
    PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-root")
    PERIOD_CHOICE = (By.XPATH, "//div[contains(text(),'сутки')]")
    COLOR_CHOICE = (By.XPATH, "//label[@for = 'black']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")
    # Кнопка Заказать во второй форме
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(), 'Заказать')]")


class LocatorCompletingOrder:
    # Кнопка "Да" при подтверждении оформлении заказа
    AGREE_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    # Кнопка Статус заказа
    WATCH_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")

