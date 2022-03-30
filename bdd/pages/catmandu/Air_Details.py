import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
import time

class air_details(BasePage):
    RETURN_TO_AIR_OPTIONS_LINK = (By.ID, "rowTop")


    def __init__(self, context):
        BasePage.__init__(self, context)


    def wait_results_upsell(self):
        element = WebDriverWait(self.context.browser, 120).until(EC.element_to_be_clickable
                                                                 ((By.ID, "rowTop")))

    def click_onChoose_flight_option_byUniqueId(self, uniqueId):
        tabId = self.context.browser.execute_script('return $tabId')
        self.context.catmandu_air_result_page_air_options_list = self.context.browser.execute_script(
            f"PostAirDetails('/Air/Details/{tabId}/{uniqueId}', '{uniqueId}')")


    def click_onFlight_option_with_upsell_enabled(self):
        self.context.catmandu_air_result_page_air_options_list = self.context.browser.execute_script(
            'return $airResults')
        assert self.context.catmandu_air_result_page_air_options_list is not None, f"No air results on air results page"
        assert len(self.context.catmandu_air_result_page_air_options_list) > 0, f"No air results on air results page"
        index = 0
        for itm in self.context.catmandu_air_result_page_air_options_list:
            if itm['UpSellEnabled']:
                self.click_onChoose_flight_option_byUniqueId(itm['UniqueID'])
                return
            else:
                index = index + 1
        raise Exception("No upsell option was found")

    def wait_for_upsell_options(self):
        element = WebDriverWait(self.context.browser, 120).until(
            EC.element_to_be_clickable(self.RETURN_TO_AIR_OPTIONS_LINK))

    def choose_max_price_upsell_option(self):
        fare_families = self.context.browser.execute_script('return $fareCombinations')
        fare_families.sort(key=lambda itm: itm['CombinationTotalAmount'], reverse=True)
        select_fare_families = fare_families[0]
        index = 1
        for i in select_fare_families['FareFamilyName']:
            if 'upsell' in i:
                is_azul_fare = False
            else:
                is_azul_fare = True

        for i in select_fare_families['FareFamilyCodes']:
            if is_azul_fare:
                self.context.browser.execute_script(f"SelectBySector('{i}', {index})")

            else:
                self.context.browser.execute_script(f"SelectBySector('{i}', null)")
            index = index + 1

    def click_button_upsell_continue(self):
        self.context.browser.execute_script(f"SetOptionsAndContinue()")




