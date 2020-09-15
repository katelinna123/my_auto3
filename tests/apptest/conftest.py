import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def appium(variables):
    caps = variables.get('caps')
    server = variables.get('server')
    driver = webdriver.Remote(server, caps)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def launch_close_app(appium):
    appium.launch_app()
    yield
    appium.close_app()
