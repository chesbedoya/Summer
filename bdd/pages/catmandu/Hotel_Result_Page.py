import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
import time


class hotel_result_page(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    def search_hotel(self, city, check_future_days, check_out_future_days, occupancy):
        combination = self.translate_combination(occupancy)
        check_in = datetime.datetime.now() + datetime.timedelta(days=check_future_days)
        check_out = datetime.datetime.now() + datetime.timedelta(days=check_out_future_days)

        sc = None if self.context.sucursal is None else self.context.sucursal
        url = "{}/{}/Hotel/{}/{}/{}/{}/NA/{}-".format(self.context.base_url,
                                                      self.context.language,
                                                      city, check_in.strftime("%Y-%m-%d"),
                                                      check_out.strftime("%Y-%m-%d"),
                                                      combination,
                                                      self.context.userservice)
        occupancy_org = occupancy.lower()
        self.context.combination_org = occupancy_org
        url = url if sc is None else f"{url}-{sc}"
        self.context.url_search = url
        #self.context.logger.debug(f'Url to search in: {url}')
        self.context.browser.get(url)
        time.sleep(10000)

    def translate_combination(self, occupancy):
        """Traduce el occupancy ingresado para que lo entienda la url
        """
        occupancy = occupancy.lower()

        if occupancy == '1r1a':
            occupancy = '1$0'
        self.context.occupancy = occupancy
        return occupancy