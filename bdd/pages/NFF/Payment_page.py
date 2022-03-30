from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from bdd.Mockaroo.MockarooRequest import MockarooRequest
#from selenium.webdriver.support.ui import Select
#from bdd.Extensions.BddExtensions import Extensions
#from selenium.common.exceptions import TimeoutException
import time

class Payment_page(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    def wait_process_payment(self):
        element = WebDriverWait(self.context.browser, 60).until(EC.element_to_be_clickable
                                                       ((By.CSS_SELECTOR, "[id$=_btnDisplay]")))
        self.payment_itinerary_number()
        element.click()

    def payment_itinerary_number(self):
        self.context.itinerary_number = WebDriverWait(self.context.browser, 60).until(EC.visibility_of_element_located
                                                       ((By.CSS_SELECTOR, "[id$=_lblReference]"))).text
        return self.context.itinerary_number

    def wait_display_page(self):
        WebDriverWait(self.context.browser, 60).until(EC.element_to_be_clickable
                                                       ((By.CSS_SELECTOR, "[id$=_btnPrintItinerary]")))

    def get_status_reservation(self):
        WebDriverWait(self.context.browser, 60).until(EC.visibility_of_element_located
                                                      ((By.XPATH, "//div[@class='status']/span")))
        view_status = self.context.browser.find_elements(By.XPATH,  "//div[@class='status']/span")
        print(view_status)
        for i in range(len(view_status)):
            get_status = view_status[i].text
            status = ['Emitido', 'Confirmada']
            assert get_status in status

