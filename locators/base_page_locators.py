from selenium.webdriver.common.by import By


class LocatorLogo:
    # Лого Самокат
    SCOOTER_LOGO = (By.XPATH, "//a[@class = 'Header_LogoScooter__3lsAR']")
    # Лого Яндекс
    YANDEX_LOGO = (By.XPATH, "//img[@alt = 'Yandex']")


class LocatorCookie:
    # Кнопка принятия Куки
    BUTTON = (By.CLASS_NAME, "App_CookieButton__3cvqF")
