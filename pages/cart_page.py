from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BaseClass):

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_CONTAINER = (By.ID, "cart_contents_container")
    CHECKOUT_BTN = (By.ID, "checkout")

    def wait_for_cart_page(self):
        self.wait.until(EC.presence_of_element_located(self.CART_CONTAINER))

    def click_checkout(self):
        self.wait_for_cart_page()
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()
