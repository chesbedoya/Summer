from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class Netadmin_page(BasePage):

    NETFARE_ONE_MOMENT_MESSAGE = (By.ID, "ctl00_lblLoadingPage")
    NETFARE_RESERVATION_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_MainMenuControl_btnCreateItinerary")
    NFF_WAIT_ITINERARY = "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_RemarkControl_btnAdd"

    def __init__(self, context):
        BasePage.__init__(self, context)

    def wait_loading_netadmin(self):
        while True:
            element = WebDriverWait(self.context.browser, 15).until(
                EC.presence_of_element_located(self.NETFARE_ONE_MOMENT_MESSAGE))
            if not element.is_displayed():
                return False

    def wait_page_netadmin(self):
        try:
            WebDriverWait(self.context.browser, 60).until(
                EC.visibility_of_element_located(self.NETFARE_RESERVATION_BUTTON))
            self.context.IsLoggedInNetAdmin = True
        except:
            self.context.IsLoggedInNetAdmin = False

    def insert_itinerary_number_in_netadmin(self):
        try:
            WebDriverWait(self.context.browser, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id$=_txtSearch]")))
            element = self.context.browser.find_element_by_css_selector('[id$=_txtSearch]')
            element.send_keys(self.context.itinerary_number, Keys.ENTER)
            webdriver.ActionChains(self.context.browser).send_keys(Keys.ESCAPE).perform()
        except:
            print("I do not enter the itinerary")

    def wait_button_comments(self):
        WebDriverWait(self.context.browser, 80).until(
            EC.element_to_be_clickable((By.ID, self.NFF_WAIT_ITINERARY)))

    def wait_button_cancel_itinerary(self):
        WebDriverWait(self.context.browser, 30).until(EC.element_to_be_clickable
                                                      ((By.CSS_SELECTOR, "[id$=_btnCancelItinerary]"))).click()
        alert = self.context.browser.switch_to.alert
        alert.accept()


