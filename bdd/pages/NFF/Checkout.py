import time

from selenium.common.exceptions import TimeoutException

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
    input_tokenex = (By.ID, 'data')
    month_credit_number =\
        'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl01_ddlCardExpireMonth'
    ID_YEAR = "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl01_ddlCardExpireYear"
    id_first_name_credit_card = (By.CSS_SELECTOR, "[id$=_txtShopperFirstName]")
    id_last_name_credit_card = (By.CSS_SELECTOR, "[id$=txtShopperLastName]")
    id_document_shopper = (By.CSS_SELECTOR, "[id$=txtDocNumberP2P]")
    id_email_shopper = (By.CSS_SELECTOR, "[id$=txtEmailP2P]")
    id_phone_number_shopper = (By.CSS_SELECTOR, "[id$=txtPhoneP2P]")
    id_address_shopper = (By.CSS_SELECTOR, "[id$=txtStreetP2P]")
    id_gender_shopper = (By.CSS_SELECTOR, "[id$=ddlGender]")
    id_street_shopper = (By.CSS_SELECTOR, "[id$=txtStreet]")
    id_click_button_payment = (By.CSS_SELECTOR, "[id$=btnPaymentMethodCC]")

    def __init__(self, context):
        BasePage.__init__(self, context)

    def wait_checkout_page(self):
        WebDriverWait(self.context.browser, 120).until(
            EC.element_to_be_clickable(self.payment_button))

    def obteined_checkout_price(self):
        checkout_price = self.context.browser.find_elements_by_id(
                "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl05_lblTotalAmount")
        price_result_checkout =checkout_price[0].text
        price_result_checkout_replace = price_result_checkout.replace("COP ", "").replace(".", "")
        price_checkout_float_results = float(price_result_checkout_replace)
        self.context.checkout_price_validation = price_checkout_float_results

    def validation_price_checkout(self):
        assert self.context.passenger_price_validation == self.context.checkout_price_validation

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
            self.fill_year_valid(payment_data)
            self.wait_disappear_popup_message_payment()
            extension.switch_to_frame_by_id_tokenex_code_card()
            self.fill_credit_card_security_code(payment_data)
            self.context.browser.switch_to.default_content()
            self.fill_name_credit_card(payment_data)
            self.fill_last_name_credit_card(payment_data)
            self.fill_document_shopper(payment_data)
            self.fill_email_shopper(payment_data)
            self.fill_phone_number_shopper(payment_data)
            self.fill_address_shopper(payment_data)
            self.choose_gender_shopper(payment_data)

    def fill_credit_number(self, payment_data):
        element = WebDriverWait(self.context.browser, 60).until(
            EC.element_to_be_clickable(self.input_tokenex))
        element.send_keys(payment_data['CreditCardNumber'])

    def fill_month_credit_number(self, payment_data):
        element = WebDriverWait(self.context.browser, 30).until(
            EC.element_to_be_clickable((By.ID, self.month_credit_number)))
        Select(self.context.browser.find_element_by_id(self.month_credit_number)).select_by_visible_text(payment_data['CreditCardValidMonth'])

    def fill_year_valid(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20).until(
            EC.element_to_be_clickable((By.ID, self.ID_YEAR)))
        Select(self.context.browser.find_element_by_id(self.ID_YEAR)).select_by_visible_text(payment_data['CreditCardValidYear'])

    def wait_disappear_popup_message_payment(self):
        try:
            WebDriverWait(self.context.browser, 30)\
                .until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'blockUI blockMsg blockPage')]")))

            WebDriverWait(self.context.browser, 60)\
                .until_not(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'blockUI blockMsg blockPage')]")))

        except TimeoutException:
            pass

    def fill_credit_card_security_code(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.input_tokenex))
        ele.send_keys(payment_data['CreditCardVisaSecurityCode'])

    def fill_name_credit_card(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_first_name_credit_card))
        ele.send_keys(payment_data['CreditCardName'])

    def fill_last_name_credit_card(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_last_name_credit_card))
        ele.send_keys(payment_data['CreditCardLastName'])

    def fill_document_shopper(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_document_shopper))
        ele.send_keys(payment_data['CreditCardDocumentId'])

    def fill_email_shopper(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_email_shopper))
        ele.send_keys(payment_data['BillingEmail'])

    def fill_phone_number_shopper(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_phone_number_shopper))
        ele.send_keys(payment_data['BillingPhone'])

    def fill_address_shopper(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_address_shopper))
        ele.send_keys(f"{payment_data['BillingAddress']} {payment_data['BillingAddressNumber']} "
                      f"{payment_data['BillingNeighborhood']} {payment_data['BillingPostalCode']}")

    def choose_gender_shopper(self, payment_data):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_gender_shopper))
        ele.send_keys(payment_data['BillingGender'])

    def fill_geography_information(self):
        mockaroo = Mockaroo_request()
        payment_data = mockaroo.get_geography_payment_data()
        self.fill_country('Colombia')
        self.fill_province('Caldas')
        self.fill_city('Manizales')
        self.fill_street(payment_data['BillingAddress'])

    def fill_country(self, country):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='ctl00_ctl00_NetSiteContentPlaceHolder_"
                                                        f"NetFulfillmentContentPlaceHolder_shopperPaymentInfoControl_"
                                                        f"ddlCountries']/option[text()='{country}']"))).click()

    def fill_province(self, province):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='ctl00_ctl00_NetSiteContentPlaceHolder_"
                                                        f"NetFulfillmentContentPlaceHolder_shopperPaymentInfoControl_"
                                                        f"ddlProvinces']/option[text()='{province}']"))).click()

    def fill_city(self, city):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='ctl00_ctl00_NetSiteContentPlaceHolder_"
                                                        f"NetFulfillmentContentPlaceHolder_shopperPaymentInfoControl_"
                                                        f"ddlCities']/option[text()='{city}']"))).click()

    def fill_street(self, street):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_street_shopper)).send_keys(street)

    def click_button_payment(self):
        ele = WebDriverWait(self.context.browser, 20). \
            until(EC.element_to_be_clickable(self.id_click_button_payment)).click()
