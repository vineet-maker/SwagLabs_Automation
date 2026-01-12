from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BaseClass):

    CHECKOUT_CONTAINER = (By.ID, "checkout_info_container")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")

    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def wait_for_checkout_page(self):
        self.wait.until(EC.presence_of_element_located(self.CHECKOUT_CONTAINER))

    def enter_checkout_details(self, fname, lname, zip_code):
        self.wait_for_checkout_page()

        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)).send_keys(fname)
        self.driver.find_element(*self.LAST_NAME).send_keys(lname)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        ).text
