from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from bdd.Mockaroo.MockarooRequest import MockarooRequest
from selenium.webdriver.support.ui import Select
#from bdd.Extensions.BddExtensions import Extensions
#from selenium.common.exceptions import TimeoutException

class Checkout(BasePage):
    payment_button = (By.CLASS_NAME, "divPaymentButtons")
    click_button_tdc = (By.CSS_SELECTOR, "[id$=_lblCCTitle]")

    def __init__(self, context):
        BasePage.__init__(self, context)

    def wait_checkout_page(self):
        WebDriverWait(self.context.browser, 120).until(
            EC.element_to_be_clickable(self.payment_button))

    def click_credit_card_payment_form(self):
        WebDriverWait(self.context.browser, 60).until(
            EC.element_to_be_clickable(self.click_button_tdc)).click()