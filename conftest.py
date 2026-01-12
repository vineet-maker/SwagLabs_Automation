import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--start-maximized")

    # Selenium Manager automatically handles ChromeDriver
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
