import pytest
from selenium import webdriver as wd


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", type=str)


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = None
    
    if browser_name == "firefox":
        driver = wd.Firefox()
    elif browser_name == "chrome":
        driver = wd.Chrome()
    
    driver.get('https://qa-scooter.praktikum-services.ru')
    yield driver
    
    driver.quit()
