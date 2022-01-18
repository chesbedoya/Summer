from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.Mockaroo.Mockaroo_request import Mockaroo_request
from selenium.webdriver.support.ui import Select
from bdd.Extensions.behave_extensions import behave_extensions
#from selenium.common.exceptions import TimeoutException

class Checkout(BasePage):
    payment_button = (By.CLASS_NAME, "divPaymentButtons")
    click_button_tdc = (By.CSS_SELECTOR, "[id$=_lblCCTitle]")
    input_tokenex = (By.ID,'data')
    month_credit_number = ('ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl01_ddlCardExpireMonth')

    def __init__(self, context):
        BasePage.__init__(self, context)

    def wait_checkout_page(self):
        WebDriverWait(self.context.browser, 120).until(
            EC.element_to_be_clickable(self.payment_button))

    def click_credit_card_payment_form(self):
        WebDriverWait(self.context.browser, 60).until(
            EC.element_to_be_clickable(self.click_button_tdc)).click()

    def fill_credit_card(self, context):
        mockaroo = Mockaroo_request()
        payment_data = mockaroo.get_payment_data()
        branch = None
        extension = behave_extensions(context)
        if branch != None:
            pass
        else:
            extension.switch_to_frame_by_id_tokenex_number_card()
            self.fill_credit_number(payment_data)
            self.context.browser.switch_to.default_content()
            self.fill_month_credit_number(payment_data)


    def fill_credit_number(self, payment_data):
        element = WebDriverWait(self.context.browser, 60).until(
            EC.element_to_be_clickable(self.input_tokenex))
        element.send_keys(payment_data['CreditCardNumber'])

    def fill_month_credit_number(self, payment_data):
        element = WebDriverWait(self.context.browser, 30).until(
            EC.element_to_be_clickable((By.ID, self.month_credit_number)))
        payment_data = payment_data['CreditCardValidMonth']
        print(payment_data)
        Select(self.context.browser.find_element_by_id(self.month_credit_number)).select_by_value(payment_data['CreditCardValidMonth'])




