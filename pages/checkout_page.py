from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.ZIP_CODE = (By.ID, "postal-code")
        self.CONTINUE_BTN = (By.ID, "continue")
        self.FINISH_BTN = (By.ID, "finish")
        self.SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def wait_for_checkout_page(self):
        # ✅ wait for URL change FIRST (critical for CI)
        self.wait.until(EC.url_contains("checkout-step-one"))

        # ✅ then wait for stable input field
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )

    def enter_checkout_details(self, first, last, zip_code):
        self.wait_for_checkout_page()

        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)

        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(last)

        self.driver.find_element(*self.ZIP_CODE).clear()
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_order(self):
        self.wait.until(EC.url_contains("checkout-step-two"))
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BTN)
        ).click()

    def get_success_message(self):
        self.wait.until(EC.url_contains("checkout-complete"))
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        ).text
