import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
import time


class car_result_page(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    def search_car(self, car_city_from, car_pickup_future_days, car_delivery_future_days):

        pickup_date = datetime.datetime.now() + datetime.timedelta(days=car_pickup_future_days)
        delivery_date = datetime.datetime.now() + datetime.timedelta(days=car_delivery_future_days)

        suc = None if self.context.sucursal is None else self.context.sucursal

        url = "{}/{}/Car/Airport/{}/{}/1000/Airport/{}/{}/1000/NA/NA/NA/{}-hide" \
            .format(self.context.base_url,
                    self.context.language,
                    car_city_from,
                    pickup_date.strftime("%Y-%m-%d"),
                    car_city_from,
                    delivery_date.strftime("%Y-%m-%d"),
                    self.context.userservice
                    )

        url = url if suc is None else f"{url}-{suc}"
        self.context.url_search = url
        #self.context.logger.debug(f'Url to search in: {url}')
        self.context.browser.get(url)

    def wait_car_results(self):
        element = WebDriverWait(self.context.browser, 120) \
            .until(EC.element_to_be_clickable((By.ID, "divCarResults")))
        self.context.catmandu_car_result_page_car_list = \
            self.context.browser.execute_script('return $searchData.CarResults')
        self.context.current_product = 'car'

    def select_option_car(self, option):

        if option == "mas barata":

            self.context.catmandu_car_result_page_lower_price_list = ('Enumerable.from($searchData.CarResults).orderBy("$.PricePayNowFrom").toArray()')
            self.context.browser.execute_script(self.context.catmandu_car_result_page_lower_price_list)
            self.fill_car_page_variables(0, 0)

        elif option == "mas cara":

            self.context.catmandu_car_result_page_high_price_list = \
                self.context.browser.execute_script('return Enumerable.from($searchData.CarResults)'
                                                    '.orderByDescending("$.PricePayNowFrom").toArray()')
            self.fill_car_page_variables(0, 0)

        elif int(option) > 0:
            self.iterate_car_result_list(option)

    def iterate_car_result_list(self, option):
        self.context.catmandu_car_result_page_car = self.context.browser.execute_script('return $searchData.CarResults')
        car_results = self.context.catmandu_car_result_page_car
        vehicle_group_counter = -1
        i = 0
        for grouped_vehicles in car_results:
            vehicle_group_counter += 1
            vehicle_option_counter = -1
            for vehicle_option in grouped_vehicles['VehicleOptions']:
                i = i + 1
                vehicle_option_counter += 1
                if i == option:
                    self.fill_car_page_variables(vehicle_group_counter, vehicle_option_counter)
                    break
            else:
                continue
            break

    def fill_car_page_variables(self, vehicle_group, vehicle_option):
        car_results = self.context.catmandu_car_result_page_car
        car_unique_id = car_results[vehicle_group]['VehicleOptions'][vehicle_option][
            'UniqueID']
        car_rate_id = \
            car_results[vehicle_group]['VehicleOptions'][vehicle_option]['Rates'][0]['Id']
        car_price = car_results[vehicle_group]['VehicleOptions'][vehicle_option][
            'AmountPricePayNow']
        rate_code = car_results[vehicle_group]['VehicleOptions'][vehicle_option]['Rates'][0]['RateCode']

        script = "return VehicleController.selectCarOption('{}', '{}', '{}', {}, '/')".format(car_unique_id,
                                                                                              car_rate_id, rate_code,
                                                                                              car_price)
        car_option_select = self.context.browser.execute_script(script)

    def continue_button_click(self):
        script = 'return VehicleController.selectCarRate()'
        click_button = self.context.browser.execute_script(script)