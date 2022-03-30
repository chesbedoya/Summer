import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
import time


class air_result_page(BasePage):
    RETURN_AIR_RESULTS = 'return $airResults'

    def __init__(self, context):
        BasePage.__init__(self, context)

    def search_air(self, airTripType, passengersCombination, airCityFrom, airCityTo, airDepartureFutureDays,
                     airReturnFutureDays, airLineCode):
        occupancy = self.translate_combination(passengersCombination)
        departureDate = datetime.datetime.now() + datetime.timedelta(days=airDepartureFutureDays)
        returnDate = None if airReturnFutureDays is None else datetime.datetime.now() + \
                                                              datetime.timedelta(days=airReturnFutureDays)
        suc = None if self.context.sucursal is None else self.context.sucursal
        if airTripType.lower() == "ow" and returnDate is None:
            url = "{}/{}/Air/{}/{}/{}/{}/{}/NA/{}/NA/NA/NA/false/false/{}-" \
                .format(self.context.base_url,
                        self.context.Language,
                        airTripType,
                        airCityFrom,
                        airCityTo,
                        departureDate.strftime("%Y-%m-%d"),
                        occupancy,
                        "NA" if airLineCode is None else airLineCode,
                        self.context.userservice
                        )
        elif airTripType.lower() == "rt" and returnDate:
            url = "{}/{}/Air/{}/{}/{}/{}/{}/{}/NA/{}/NA/NA/NA/false/false/{}-" \
                .format(self.context.base_url,
                        self.context.language,
                        airTripType,
                        airCityFrom,
                        airCityTo,
                        departureDate.strftime("%Y-%m-%d"),
                        returnDate.strftime("%Y-%m-%d"),
                        occupancy,
                        "NA" if airLineCode is None else airLineCode,
                        self.context.userservice
                        )
        else:
            raise NotImplementedError(u'air trip type is not implemented..... falta implementar esta parte del código')

        url = url if suc is None else f"{url}-{suc}"
        self.context.url_search = url
        self.context.air_return_date_change = returnDate
        self.context.browser.get(url)

    def translate_combination(self, occupancy):
        """Traduce el occupancy ingresado para que lo entienda la url
        """
        occupancy = occupancy.lower()

        if occupancy == '1adt':
            occupancy = '1/0/0'

        if occupancy == '1adt1chd':
            occupancy = '1/1/0'

        if occupancy == '1adt1chd1inf':
            occupancy = '1/1/1'
        return occupancy


    def wait_results_air(self):
        element = WebDriverWait(self.context.browser, 120).until(EC.element_to_be_clickable
                                                                 ((By.ID, "divAirResults")))
        self.context.catmandu_air_result = self.context.browser.execute_script(self.RETURN_AIR_RESULTS)
        self.context.current_product = 'air'

    def click_with_upsell_enabled(self):
        self.context.air_result_page = self.context.browser.execute_script('return $airResults')
        index=0
        for i in self.context.air_result_page:
            if i['UpSellEnabled']:
                self.click_option(i['UniqueID'])
                return
            else:
                index=index+1
        raise Exception('upsell_not_found')

    def click_option(self, UniqueID):
        tab_id = self.context.browser.execute_script('return $tabId')
        self.context.option_upsell_enabled = self.context.browser.execute_script(f"PostAirDetails('/Air/Details/{tab_id}/{UniqueID}', '{UniqueID}')")
