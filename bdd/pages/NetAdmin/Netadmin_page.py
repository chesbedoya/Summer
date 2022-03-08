from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.Extensions.behave_extensions import behave_extensions


class Netadmin_page(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    def insert_itinerary_number_in_netadmin(self):
        WebDriverWait(self.context.browser, 40).until(EC.element_to_be_clickable
                                                      ((By.CSS_SELECTOR, "[id$=_txtSearch]"))).send_keys(
                                                                                        self.context.itinerary_number)

    def click_button_search(self):
        WebDriverWait(self.context.browser, 40).until(EC.element_to_be_clickable
                                                      ((By.CSS_SELECTOR, "[id$=_btnSearch]"))).click()

    def wait_button_comments(self):
        WebDriverWait(self.context.browser, 60).until\
            (EC.visibility_of_element_located((By.ID, "ctl00_ctl00_NetSiteContentPlaceHolder_"
                                                     "NetFulfillmentContentPlaceHolder_RemarkControl_btnAdd")))

    def wait_button_cancel_itinerary(self):
        WebDriverWait(self.context.browser, 30).until(EC.element_to_be_clickable
                                                      ((By.CSS_SELECTOR, "[id$=_btnCancelItinerary]"))).click()
        alert = self.context.browser.switch_to.alert
        alert.accept()

