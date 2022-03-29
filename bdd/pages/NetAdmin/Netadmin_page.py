from selenium.common.exceptions import TimeoutException
from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class Netadmin_page(BasePage):

    NETFARE_ONE_MOMENT_MESSAGE = (By.ID, "ctl00_lblLoadingPage")
    NETFARE_RESERVATION_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_MainMenuControl_btnCreateItinerary")
    NETFARE_CANCEL_RESERVATION = (By.ID, "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_btnCancelItinerary")
    NETFARE_MESSAGE_NOTIFICATION_CANCEL_ITINERARY = (By.ID, "divNotify")
    NFF_WAIT_ITINERARY = (By.ID, "ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_RemarkControl_btnAdd")
    NETFARE_INPUT_ITINERARY = (By.ID, "ctl00_ContentPlaceHolder1_txtSearch")

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
            element = WebDriverWait(self.context.browser, 40).until(
                EC.element_to_be_clickable(self.NETFARE_INPUT_ITINERARY))
            available = element.is_enabled()
            if available:
                element.send_keys(self.context.itinerary_number, Keys.ESCAPE)
                webdriver.ActionChains(self.context.browser).send_keys(Keys.TAB).perform()
                webdriver.ActionChains(self.context.browser).send_keys(Keys.ENTER).perform()
            else:
                print("No ingreso el itinerario")
        except Exception as e:
            print('Not Itinerary' + str(e))

    def wait_loading_itinerary(self):
        try:
            while True:
                WebDriverWait(self.context.browser, 60).until(
                    EC.element_to_be_clickable((By.XPATH, "//td[@class='tab-text']")))
                element = self.context.browser.find_elements_by_xpath("//td[@class='tab-text']")
                var = element[0].text
                if var != 'Cargando' and var != 'Nueva Pestaña':
                    break
        except Exception as e:
            print('Not loading display' + str(e))

    def wait_button_cancel_itinerary(self):
        WebDriverWait(self.context.browser, 60).until(
            EC.visibility_of_element_located(self.NETFARE_CANCEL_RESERVATION)).click()
        alert = self.context.browser.switch_to.alert
        alert.accept()

    def cancel_message_itinerary(self):
        try:
            WebDriverWait(self.context.browser, 20) \
                .until(EC.presence_of_element_located(self.NETFARE_MESSAGE_NOTIFICATION_CANCEL_ITINERARY))

            WebDriverWait(self.context.browser, 20) \
                .until_not(EC.presence_of_element_located(self.NETFARE_MESSAGE_NOTIFICATION_CANCEL_ITINERARY))

        except TimeoutException:
            pass

    def validation_cancel_itinerary(self):
        WebDriverWait(self.context.browser, 60) \
<<<<<<< HEAD
            .until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl02_lblStatus']")))
        set_state = self.context.browser.find_elements(By.XPATH, "//*[@id='ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl02_lblStatus']")
        state = set_state[0].text
        assert state in "Cancelado"
=======
            .until(EC.visibility_of_element_located((By.XPATH, "//div[@class='status']/span[@class='Cancelled']")))
        state = self.context.browser.find_elements(By.XPATH, "//div[@class='status']/span[@class='Cancelled']")
        set_state = state[0].text
        assert_state = ['Cancelado', 'Cancelado Offline']
        assert set_state in assert_state
>>>>>>> victorino

    def wait_button_comments(self):
        WebDriverWait(self.context.browser, 80).until(
            EC.element_to_be_clickable(self.NFF_WAIT_ITINERARY))



