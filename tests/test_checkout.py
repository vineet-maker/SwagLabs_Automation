from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import Config

def test_complete_checkout_flow(setup):
    driver = setup
    driver.get(Config.URL)

    # Login
    LoginPage(driver).login(Config.USERNAME, Config.PASSWORD)

    # Add product
    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.go_to_cart()

    # Cart
    cart = CartPage(driver)
    cart.click_checkout()

    # Checkout
    checkout = CheckoutPage(driver)
    checkout.enter_checkout_details("Vineet", "Raj", "560001")
    checkout.finish_order()

    # Validation
    assert checkout.get_success_message() == "Thank you for your order!"
