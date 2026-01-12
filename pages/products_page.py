from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass

class ProductsPage(BaseClass):

    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BACKPACK).click()

    def go_to_cart(self):
        self.wait_for_element(self.CART_ICON).click()
