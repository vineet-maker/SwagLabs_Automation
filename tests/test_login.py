import allure
from pages.login_page import LoginPage
from config.config import Config


@allure.feature("Login")
@allure.story("Valid Login")
def test_valid_login(setup):
    driver = setup
    driver.get(Config.URL)

    LoginPage(driver).login(Config.USERNAME, Config.PASSWORD)

    assert "inventory" in driver.current_url
