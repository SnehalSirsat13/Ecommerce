from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
     driver = webdriver.Chrome()
     print("Launching.......Chrome")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching.......Firefox")
    return driver


def pytest_adoption(parser):
    parser.adoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")