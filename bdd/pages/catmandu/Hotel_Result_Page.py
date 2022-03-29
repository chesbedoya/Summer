import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
import time


class hotel_result_page(BasePage):
    RETURN_HOTEL_RESULTS = 'return $HotelResults'

    def __init__(self, context):
        BasePage.__init__(self, context)

    def search_hotel(self, city, check_future_days, check_out_future_days, occupancy):
        combination = self.translate_combination(occupancy)
        check_in = datetime.datetime.now() + datetime.timedelta(days=check_future_days)
        check_out = datetime.datetime.now() + datetime.timedelta(days=check_out_future_days)

        sc = None if self.context.sucursal is None else self.context.sucursal
        print (sc)
        url = "{}/{}/Hotel/{}/{}/{}/{}/NA/{}".format(self.context.base_url,
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
        #time.sleep(10000)

    def translate_combination(self, occupancy):
        """Traduce el occupancy ingresado para que lo entienda la url
        """
        occupancy = occupancy.lower()

        if occupancy == '1r1a':
            occupancy = '1$0'

        elif occupancy == '1r2a':
            occupancy = '2$0'

        elif occupancy == '1r2a1c':
            occupancy = '2-8$0'
        self.context.occupancy = occupancy
        return occupancy

    def wait_results_hotel(self):
        element = WebDriverWait(self.context.browser, 120).until(EC.element_to_be_clickable
                                                                 ((By.ID, "divHotelResults")))
        self.context.catmandu_hotel_result = self.context.browser.execute_script(self.RETURN_HOTEL_RESULTS)
        self.context.current_product = 'hotel'

    def click_option_hotel(self):
        element = WebDriverWait(self.context.browser, 120).until(EC.element_to_be_clickable
                                                                 ((By.ID, "Hot_0_room_0_option_1"))).click()

    def delete_filter_hoteles(self):
        WebDriverWait(self.context.browser, 60) \
            .until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='nts-tag']/a[@class='nts-tag-remove']"))).click()

    def click_hotel_option_dinamic(self, hotelOption, roomOption):
        self.context.selectedHotel = self.context.catmandu_hotel_result[hotelOption]
        combined_hotel = len(self.context.selectedHotel['CombinedRoomTypeAvailability'])
        is_combined = True if combined_hotel > 0 else False
        if is_combined:
            select_room_option = self.context.selectedHotel['CombinedRoomTypeAvailability'][roomOption]
            self.context.browser.execute_script(
                f"selectHotelOption('Hot_{hotelOption}_comb_{select_room_option['Id']}', 'bundled', false)")

        else:
            hotelOption = hotelOption + 1
            not_combined = self.context.catmandu_hotel_result[hotelOption]
            not_combined_room = not_combined['RoomTypeAvailability'][0]['RoomOptions'][roomOption]
            self.context.browser.execute_script(
                f"selectHotelOption('Hot_{hotelOption}_room_{roomOption}_option_{not_combined_room['Id']}','perRoom', false)")


