from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Netadmin_page(BasePage):
    NFF_WAIT_ITINERARY = "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_RemarkControl_btnAdd"

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
        WebDriverWait(self.context.browser, 80).until(
            EC.visibility_of_element_located((By.ID, self.NFF_WAIT_ITINERARY)))

    def wait_button_cancel_itinerary(self):
        WebDriverWait(self.context.browser, 30).until(EC.element_to_be_clickable
                                                      ((By.CSS_SELECTOR, "[id$=_btnCancelItinerary]"))).click()
        alert = self.context.browser.switch_to.alert
        alert.accept()

