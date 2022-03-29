import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
import time


class extras_result_page(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    def search_extra(self, extra_city_from, extra_start_future_days, extra_end_future_days, occupancy):
        extra_start_date = datetime.datetime.now() + datetime.timedelta(days=extra_start_future_days)
        extra_end_date = datetime.datetime.now() + datetime.timedelta(days=extra_end_future_days)

        suc = None if self.context.sucursal is None else self.context.sucursal

        url = "{}/{}/Extras/{}/NA/{}/{}/{}-".format(self.context.base_url,
                                                    self.context.language,
                                                    extra_city_from,
                                                    extra_start_date.strftime("%Y-%m-%d"),
                                                    extra_end_date.strftime("%Y-%m-%d"),
                                                    self.context.userservice
                                                    )

        self.context.extra_start_date = extra_start_date

        url = url if suc is None else f"{url}-{suc}"
        self.context.url_search = url
        occupancy = occupancy.lower()
        self.context.ocupation_extra = occupancy
        self.context.browser.get(url)

    def wait_extra_results(self):
        element = WebDriverWait(self.context.browser, 120) \
            .until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "hotel-image")))
        self.context.current_product = 'extra'


    def obteined_extras_price(self):
        extras_price = self.context.browser.find_elements_by_xpath("//div[@class='reprice header']//div[@class='currencyText price-extra money']//span[@class='currencyText']")
        price_result_extras = extras_price[0].text
        price_result_extras_replace = price_result_extras.replace("$ ", "").replace(".", "")
        price_extras_float_results = float(price_result_extras_replace)
        self.context.extras_price_options = price_extras_float_results

    def select_option_extra(self, option):
        option = option - 1
        try:
            element = WebDriverWait(self.context.browser, 120)\
                .until(EC.visibility_of_element_located((By.XPATH,
                                                         "//div[@class='column column-block no-button extraResult']")))

            option_extras = self.context.browser.find_elements(
                By.XPATH, "//div[@class='column column-block no-button extraResult']")
            assert len(option_extras) > 0
            option_extras[option].click()

        except TimeoutError:
            print("No se esta efectuando la espera")

    def wait_extra_results_crosselling(self):
        element = WebDriverWait(self.context.browser, 120) \
            .until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "hotel-image")))

    def wait_product_view(self):
        WebDriverWait(self.context.browser, 120).until(EC.visibility_of_element_located((By.ID, 'btnPurchase_1')))

    def load_quantity_person(self):
        WebDriverWait(self.context.browser, 30).until(
            EC.visibility_of_element_located((By.ID, 'ddl_Prod_0')))
        Select(self.context.browser.find_element_by_id('ddl_Prod_0')).select_by_value("1")

    def click_button_purchase(self):
        self.context.browser.execute_script(
            "return purchaseItems(false, 1, true)")