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

    def fill_passenger_information(self):
        occupancy = self.get_occupancy_model()
        data = self.mockaroo.get_information_passenger_data()
        if occupancy == '1r1a' or occupancy == '1adt':
            self.fill_passenger1r1a()
            self.fill_email(data['Email'])
            self.fill_phone(data['Phone'])
            self.click_checkbox()

        if occupancy == '1r2a' or occupancy == '2adt':
            self.fill_passenger1r2a()
            self.fill_email(data['Email'])
            self.fill_phone(data['Phone'])
            self.click_checkbox()

    def fill_passenger1r1a(self):
        self.fill_form_passenger('primary_adult', 0)

    def fill_passenger1r2a(self):
        self.fill_form_passenger('primary_adult', 0)
        self.fill_form_passenger('secondary_adult', 1)


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
        else:
            rooms = search_json['Rooms']
            adults_rooms_one = 0
            if len(rooms) == 1:
                guests = search_json['Rooms'][0]['Guests']
                for i in guests:
                    if i['Type'] == 0:
                        adults_rooms_one = adults_rooms_one + 1
            occupancy = self.make_occupancy(len(rooms), adults_rooms_one)
            return occupancy

    def make_occupancy(self, rooms, adults_rooms_one):
        if rooms == 1:
            if adults_rooms_one == 1:
                return '1r1a'
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
