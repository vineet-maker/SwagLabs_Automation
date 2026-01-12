from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.PAGE_TITLE = (By.CLASS_NAME, "title")
        self.ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
        self.CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        ).text

    def add_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTN)
        ).click()

    def get_cart_count(self):
        self.wait.until(
            EC.presence_of_element_located(self.CART_BADGE)
        )
        badge = self.driver.find_element(*self.CART_BADGE)

        self.wait.until(lambda d: badge.text != "")
        return badge.text

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()
