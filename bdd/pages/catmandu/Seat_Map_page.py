from selenium.common.exceptions import StaleElementReferenceException
from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime


class seat_map_page(BasePage):
    SEAT_CONTROL_TAG_NAME = "app-seat"
    SEAT_CONTROL = (By.TAG_NAME, SEAT_CONTROL_TAG_NAME)
    AIR_PLANE_MAP = (By.ID, "seatMapSection")
    ITINERARY_CONTROL = "app-itinerary"
    LOADER_CLASSNAME = (By.CLASS_NAME, "loader-grid")
    POPUP_SEAT_CONFIRMATION_CLASSNAME = (By.CLASS_NAME, "swal2-popup")
    CONFIRM_BUTTON = (By.CLASS_NAME, "button-confirm")
    CONFIRM_BUTTON_POPUP = (By.CLASS_NAME, "swalConfirmButton")
    SEAT_AIR_EXCHANGE = (By.ID, "exchange-component")

    def __init__(self, context):
        BasePage.__init__(self, context=context)

    def WaitUntilSeatmapIsShown(self):
        element = WebDriverWait(self.context.browser, 120).until(EC.presence_of_element_located(self.SEAT_CONTROL))