from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.config import Config

def test_add_product_to_cart(setup):
    driver = setup
    driver.get(Config.URL)

    LoginPage(driver).login(Config.USERNAME, Config.PASSWORD)
    products = ProductsPage(driver)

    assert products.get_title() == "Products"

    products.add_product_to_cart()
    assert products.get_cart_count() == "1"
