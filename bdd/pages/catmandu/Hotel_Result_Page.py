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

        elif occupancy == '2r4a1c':
            occupancy = '2-8$0!2$0'

        elif occupancy == '2r4a1c1i':
            occupancy = '2-1$0!2-8$0'
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
        """
        Selecting a room being a hotel bundled and not bundled
        :param hotelIndex: dynamic hotel value int
        :param roomIndex: dynamic room value int
        :return
        """
        hotel_result = self.context.browser.execute_script(self.RETURN_HOTEL_RESULTS)
        assert len(hotel_result) > 0
        selected_hotel = hotel_result[hotelOption]
        combined_hotel = len(selected_hotel['CombinedRoomTypeAvailability'])
        is_combined_hotel = True if combined_hotel > 0 else False
        number_hotel = selected_hotel['UniqueID']
        if is_combined_hotel:
            assert len(selected_hotel['CombinedRoomTypeAvailability']) > 0
            selected_room = selected_hotel['CombinedRoomTypeAvailability'][roomOption]
            validate_refundable = selected_hotel['CombinedRoomTypeAvailability'][roomOption]['RefundableType']
            assert validate_refundable == 0
            self.context.browser.execute_script(
                f"selectHotelOption('{number_hotel}_comb_{selected_room['Id']}', 'bundled', false)")
        else:
            assert len(selected_hotel['RoomTypeAvailability']) > 0
            selected_room_option = selected_hotel['RoomTypeAvailability'][0]['RoomOptions'][roomOption]['Id']
            self.context.browser.execute_script(
                f"selectHotelOption('{number_hotel}_room_{roomOption}_option_{selected_room_option}', 'perRoom', false)")

    def obtained_hotel_price(self, context, hotel_option, room_option):
        WebDriverWait(self.context.browser, 120)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                                     "//div[@class='roomOptPrice text-right large-text-right']//span[@class='currencyText']")))
        view_price = self.context.browser.find_elements(By.XPATH,
                                                        "//div[@class='roomOptPrice text-right large-text-right']//span[@class='currencyText']")

        convert_price_hotel = view_price[room_option].text
        convert_price_hotel = convert_price_hotel.replace('.', '')
        convert_price_hotel = convert_price_hotel.replace('$ ', '')
        convert_price_hotel = (float(convert_price_hotel))

        hotel_result = self.context.browser.execute_script('return $HotelResults')
        context.validate_bundled = len(hotel_result[hotel_option]['CombinedRoomTypeAvailability'])

        context.flow_occupancy = self.context.occupancy
        if context.validate_bundled > 0:
            context.price_obtained_in_hotel_result_page = convert_price_hotel
        else:
            hotel_result = self.context.browser.execute_script('return $HotelResults')
            print(hotel_result)
            context.validate_no_bundled = len(hotel_result[hotel_option]['RoomTypeAvailability'])
            if context.validate_no_bundled == 2:
                context.price_second = hotel_result[hotel_option]['RoomTypeAvailability'][1]['RoomOptions'][0]['Amount']
                context.price_obtained_in_hotel_result_page = (convert_price_hotel + context.price_second)

            else:
                context.price_obtained_in_hotel_result_page = convert_price_hotel

        return context.price_obtained_in_hotel_result_page

