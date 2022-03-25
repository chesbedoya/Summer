import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
from bdd.Mockaroo.Mockaroo_request import Mockaroo_request
import datetime



class Passenger_page(BasePage):
    PASSENGER_TITLE = "Travelers_{index}__Title"
    PASSENGER_NAME = "Travelers_{index}__FirstName"
    PASSENGER_LAST_NAME = "Travelers_{index}__LastName"
    PASSENGER_DOCUMENT_TYPE = "Travelers_{index}__DocumentType"
    PASSENGER_DOCUMENT_NUMBER = "Travelers_{index}__DucumentNumber"
    PASSENGER_NATIONALITY = "Travelers_{index}__Nationality"
    PASSENGER_DOF = "Travelers[{index}].DOB_d"
    PASSENGER_MOB = "Travelers[{index}].DOB_m"
    PASSENGER_YOB = "Travelers[{index}].DOB_y"
    PASSENGER_EMAIL = (By.ID, "ContactEmail")
    PASSENGER_PHONE = (By.ID, "ContactPhone")
    PASSENGER_CHECKBOX = "chkTermsAndConditions"
    EXTRA_TRAVELER_TITLE = "ExtraReservationItems_0__Travelers_0__Title"
    EXTRA_TRAVELER_NAME = "ExtraReservationItems_0__Travelers_0__FirstName"
    EXTRA_TRAVELER_LAST_NAME = "ExtraReservationItems_0__Travelers_0__LastName"
    EXTRA_TRAVELER_DOCUMENT_TYPE = "ExtraReservationItems_0__Travelers_0__DocumentType"
    EXTRA_TRAVELER_DOCUMENT = "ExtraReservationItems_0__Travelers_0__DucumentNumber"
    EXTRA_TRAVELER_DOB_D = "ExtraReservationItems[0].Travelers[0].DOB_d"
    EXTRA_TRAVELER_DOB_M = "ExtraReservationItems[0].Travelers[0].DOB_m"
    EXTRA_TRAVELER_DOB_Y = "ExtraReservationItems[0].Travelers[0].DOB_y"

    def __init__(self, context):
        BasePage.__init__(self, context)
        self.mockaroo = Mockaroo_request()

    def wait_for_passenger_page(self):
        WebDriverWait(self.context.browser, 120).until(EC.element_to_be_clickable
                                                       ((By.ID, "ContactEmail")))

    def wait_until_price_validation(self):
        while True:
            element = WebDriverWait(self.context.browser, 120).until(EC.presence_of_element_located
                                                       ((By.ID, "message")))
            if not element.is_displayed():
                return
    def obteined_passenger_price(self):
        passenger_price = self.context.browser.find_elements_by_xpath("//div[@class='small-8 column text-right bold']//span[@class='nts-totalizer nts-big-total']//span[@class='currencyText']")
        price_result_passenger = passenger_price[0].text
        price_result_passenger_replace = price_result_passenger.replace("$ ", "").replace(".", "")
        price_passenger_float_results = float(price_result_passenger_replace)
        self.context.passenger_price_validation = price_passenger_float_results

    def validation_price_passenger(self):
        assert self.context.hotel_price_options == self.context.passenger_price_validation

    def validation_extra_price_passenger(self):
        assert self.context.extras_price_options == self.context.passenger_price_validation

    def fill_passenger_information(self):
        occupancy = self.get_occupancy_model()
        data = self.mockaroo.get_information_passenger_data()
        if occupancy == '1r1a' or occupancy == '1adt':
            self.fill_passenger1r1a()
            self.fill_email(data['Email'])
            self.fill_phone(data['Phone'])
            self.click_checkbox()

        elif occupancy == '1r2a' or occupancy == '2adt':
            self.fill_passenger1r2a()
            self.fill_email(data['Email'])
            self.fill_phone(data['Phone'])
            self.click_checkbox()

        elif occupancy == '1r2a1c':
            self.fill_passenger1r2a1c()
            self.fill_email(data['Email'])
            self.fill_phone(data['Phone'])
            self.click_checkbox()

        elif occupancy == '1re':
            self.fill_traveler()
            self.fill_email(data['Email'])
            self.fill_phone(data['Phone'])
            self.click_checkbox()


    def fill_passenger1r1a(self):
        self.fill_form_passenger('primary_adult', 0)

    def fill_passenger1r2a(self):
        self.fill_form_passenger('primary_adult', 0)
        self.fill_form_passenger('secondary_adult', 1)

    def fill_passenger1r2a1c(self):
        self.fill_form_passenger('primary_adult', 0)
        self.fill_form_passenger('secondary_adult', 1)
        self.fill_form_passenger('primary_children', 2)

    def fill_traveler(self):
        self.fill_form_passenger('traveler', 0)


    def fill_form_passenger(self, type_passenger, passenger_number):
        data = self.mockaroo.get_information_passenger_data()
        date_time_format = '%Y-%m-%d %H:%M:%S'
        if type_passenger == 'primary_adult' or type_passenger == 'secondary_adult':
            self.fill_title(data['Title'], passenger_number)
            self.fill_name(data['FirstName'], passenger_number)
            self.fill_last_name(data['LastName'], passenger_number)
            self.fill_document_type(['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.fill_document_number(self.mockaroo.get_document_passenger(), passenger_number)
            date_object = datetime.datetime.strptime(data['AdultAge'], date_time_format)
            self.fill_birthday(date_object.day, passenger_number)
            self.fill_birthday_month(date_object.month, passenger_number)
            self.fill_birthday_year(date_object.year, passenger_number)

        elif type_passenger == 'primary_children':
            self.fill_title(data['Title'], passenger_number)
            self.fill_name(data['FirstName'], passenger_number)
            self.fill_last_name(data['LastName'], passenger_number)
            self.fill_document_type(['BillingDocumentTypeNamePlaceToPay'], passenger_number)
            self.fill_document_number(self.mockaroo.get_document_passenger(), passenger_number)
            date_object = datetime.datetime.strptime(data['ChildAge8'], date_time_format)
            self.fill_birthday(date_object.day, passenger_number)
            self.fill_birthday_month(date_object.month, passenger_number)
            self.fill_birthday_year(date_object.year, passenger_number)


        elif type_passenger == 'traveler':
            self.fill_extra_traveler_title(data['Title'])
            self.fill_extra_traveler_name(data['FirstName'])
            self.fill_extra_traveler_last_name(data['LastName'])
            self.fill_extra_traveler_document_type(data['BillingDocumentTypeNamePlaceToPay'])
            self.fill_extra_traveler_document_number(self.mockaroo.get_document_passenger())
            date_object = datetime.datetime.strptime(data['AdultAge'], date_time_format)
            self.fill_extra_traveler_birth_day(date_object.day)
            self.fill_extra_traveler_birth_month(date_object.month)
            self.fill_extra_traveler_birth_year(date_object.year)


    def get_occupancy_model(self):
        search_json = self.context.browser.execute_script('return $searchData')
        if hasattr(self.context, 'current_product') and self.context.current_product != 'hotel':
            if self.context.current_product == 'air':
                air_passengers_list = search_json['Passengers']
                quantity_air_passenger = len(air_passengers_list)
                air_adult_passenger = 0
                air_child_passenger = 0
                air_infant_passenger = 0
                for itm in air_passengers_list:
                    passenger_type = itm['Type']
                    if quantity_air_passenger == 1 and passenger_type == 0:
                        air_occupancy = '1adt'
                        return "{}".format(air_occupancy)

            elif self.context.current_product == 'extra':
                if self.context.ocupation_extra == '1re':
                    self.context.ocupation = '1re'
                return self.context.ocupation

        else:
            rooms = search_json['Rooms']
            adults_rooms_one = 0
            children_rooms_one = 0
            if len(rooms) == 1:
                guests = search_json['Rooms'][0]['Guests']
                for i in guests:
                    if i['Type'] == 0:
                        adults_rooms_one = adults_rooms_one + 1
                    elif i['Type'] == 1:
                        children_rooms_one = children_rooms_one + 1

            occupancy = self.make_occupancy(len(rooms), adults_rooms_one, children_rooms_one)
            return occupancy

    def make_occupancy(self, rooms, adults_rooms_one, children_rooms_one):
        if rooms == 1:
            if adults_rooms_one == 1:
                return '1r1a'
            elif adults_rooms_one == 2 and children_rooms_one == 1:
                return '1r2a1c'
            elif adults_rooms_one == 2:
                return '1r2a'


    def fill_title(self, title, index):
        element = (By.ID, self.PASSENGER_TITLE.replace('{index}', str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located((
                By.XPATH, f"//*[@id='Travelers_{index}__Title']/option[text()='{title}']"))).click()

    def fill_name(self, name, index):
        element = (By.ID, self.PASSENGER_NAME.replace('{index}', str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(element)).send_keys(name)

    def fill_last_name(self, last_name, index):
        element = (By.ID, self.PASSENGER_LAST_NAME.replace('{index}', str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(element)).send_keys(last_name)

    def fill_document_type(self, document_type, index):
        element = (By.ID, self.PASSENGER_DOCUMENT_TYPE.replace('{index}', str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(element)).send_keys(document_type)

    def fill_document_number(self, document_number, index):
        element = (By.ID, self.PASSENGER_DOCUMENT_NUMBER.replace('{index}', str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(element)).send_keys(document_number)

    def fill_birthday(self, day, index):
        by = (By.ID, self.PASSENGER_DOF.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='Travelers[{index}].DOB_d']/option[text()='{day}']"))).click()

    def fill_birthday_month(self, month, index):
        by = (By.ID, self.PASSENGER_MOB.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='Travelers[{index}].DOB_m']/option[text()='{month}']"))).click()

    def fill_birthday_year(self, year, index):
        by = (By.ID, self.PASSENGER_YOB.replace("{index}", str(index)))
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='Travelers[{index}].DOB_y']/option[text()='{year}']"))).click()

    def fill_email(self, email):
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(
                self.PASSENGER_EMAIL)).send_keys(email)

    def fill_phone(self, phone):
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(
                self.PASSENGER_PHONE)).send_keys(phone)

    def click_checkbox(self):
        WebDriverWait(self.context.browser, 20).until(
            EC.element_to_be_clickable(
                (By.ID, 'chkTermsAndConditions'))).click()

    def click_button_continue(self):
        WebDriverWait(self.context.browser, 20).until(
            EC.element_to_be_clickable(
                (By.ID, 'submitButtonId'))).click()


    def fill_extra_traveler_title(self, title):
        by = (By.ID, self.EXTRA_TRAVELER_TITLE)
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[@id='ExtraReservationItems_0__Travelers_0__Title']/option[text()='{title}']"))).click()

    def fill_extra_traveler_name(self, name):
        by = (By.ID, self.EXTRA_TRAVELER_NAME)
        name = re.sub(r"[^\w.@-]", "", name)
        #name = name.replace("'", "") if "'" in name else name
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(by)).send_keys(name)

    def fill_extra_traveler_last_name(self, last_name):
        by = (By.ID, self.EXTRA_TRAVELER_LAST_NAME)
        last_name = re.sub(r"[^\w.@-]", "", last_name)
        #last_name = last_name.replace("'", "") if "'" in last_name else last_name
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located(by)).send_keys(last_name)

    def fill_extra_traveler_document_type(self, type_document):
        by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT_TYPE)
        WebDriverWait(self.context.browser, 30).until(
            EC.visibility_of_element_located(by)).send_keys(type_document)

    def fill_extra_traveler_document_number(self, document):
        by = (By.ID, self.EXTRA_TRAVELER_DOCUMENT)
        WebDriverWait(self.context.browser, 30).until(
            EC.visibility_of_element_located(by)).send_keys(document)

    def fill_extra_traveler_birth_day(self, day):
        by = (By.ID, self.EXTRA_TRAVELER_DOB_D)
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[@id='ExtraReservationItems[0].Travelers[0].DOB_d']/option[text()='{day}']"))).click()

    def fill_extra_traveler_birth_month(self, month):
        by = (By.ID, self.EXTRA_TRAVELER_DOB_M)
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[@id='ExtraReservationItems[0].Travelers[0].DOB_m']/option[text()='{month}']"))).click()

    def fill_extra_traveler_birth_year(self, year):
        by = (By.ID, self.EXTRA_TRAVELER_DOB_Y)
        WebDriverWait(self.context.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[@id='ExtraReservationItems[0].Travelers[0].DOB_y']/option[text()='{year}']"))).click()

