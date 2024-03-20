from typing import Union

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser: Union[ChromeWebDriver, FirefoxWebDriver] = browser
        self.wait = WebDriverWait(browser, 10)

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def find_and_click_element(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        elem.click()
        return elem

    def click_on_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()

    def get_text_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def accept_cookies(self, locator):
        self.find_element(locator).click()

    def find_element_send_keys(self, locator, value):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(value)

    def current_url(self):
        return self.browser.current_url

    def switch_to(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def url_to_be(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))
