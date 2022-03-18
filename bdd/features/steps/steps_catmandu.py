import time
from behave import *
from bdd.pages.catmandu.Hotel_Result_Page import hotel_result_page
from bdd.pages.catmandu.Air_Result_Page import air_result_page
from bdd.pages.catmandu.Passenger_page import Passenger_page
from bdd.pages.catmandu.Air_Details import air_details


@Given("Hacer búsqueda de hoteles en catmandu para ocupación {occupancy:w} para destino iata {destination:w}"
       " con fecha de checkin en {check_future_days:d} días y checkout en {check_out_future_days:d} días")

def step_impl(context, occupancy, destination, check_future_days, check_out_future_days):

    page = hotel_result_page(context)
    page.search_hotel(city=destination, check_future_days=check_future_days, check_out_future_days=check_out_future_days
                      , occupancy=occupancy)
    context.current_page = page


@Then("Esperar que la página de resultados traiga hoteles en catmandú")
def step_impl(context):
    context.current_page.wait_results_hotel()

@Then("Quitar filtro de solo hoteles con imagenes")
def step_impl(context):
    context.current_page.delete_filter_hoteles()

@Then("Seleccionar la primera opción de hotel")
def step_impl(context):
    context.current_page.click_option_hotel()

@Then("Seleccionar la opción {roomOption:d} del hotel {hotelOption:d} de la página de resultados de catmandú")
def step_impl(context,hotelOption, roomOption):

    if hotelOption >= 1:
        hotelOption = hotelOption-1
    if roomOption >= 1:
        roomOption = roomOption-1


    page = hotel_result_page(context)
    page.obteined_hotel_price()
    page.click_hotel_option_dinamic(hotelOption, roomOption)


@Then("Esperar la página de pasajeros")
def step_impl(context):
    context.currentPage = Passenger_page(context)
    context.currentPage.wait_for_passenger_page()

@Then("Esperar la validación de precios en página de pasajeros de catmandú")
def step_impl(context):
    context.currentPage.wait_until_price_validation()


@Then("Llenar formulario de pasajeros")
def step_impl(context):
    context.currentPage.obteined_passenger_price()
    context.currentPage.validation_price_passenger()
    context.currentPage.fill_passenger_information()

@Then("Validar que el precio en la pagina de hoteles sea el mismo precio que en pagina de pasajeros")
def step_impl(context):
    context.currentPage.obteined_passenger_price()
    context.currentPage.validation_price_passenger()


@Then("Click botón continuar en página de pasajeros")
def step_impl(context):
    context.currentPage.click_button_continue()


@Given('Hacer búsqueda de aéreo en catmandu {trip_type:w} con la aerolinea {airline_code:w} para ocupación {passenger_combination:w} saliendo desde {city_from:w} con destino {city_to:w} con fecha de salida en {departure_future_days:d} días')
def step_impl(context, trip_type, airline_code, passenger_combination, city_from, city_to, departure_future_days):

    page = air_result_page(context)
    page.search_air(trip_type=trip_type, airline_code=airline_code, passenger_combination=passenger_combination,
                    city_from=city_from, city_to=city_to, departure_future_days=departure_future_days)
    context.current_page = page

@Then("Esperar que la página de resultados traiga aéreos en catmandú")
def step_impl(context):
    context.current_page.wait_results_air()

@Then("Seleccionar la primera opción con upsell")
def step_impl(context):
    context.current_page.click_with_upsell_enabled()

@Then("Esperar que la página de upsell se visualice en catmandu")
def step_impl(context):
    page = air_details(context)
    page.wait_results_upsell()
    context.currentPage = page

@Then('Seleccionar la opción "{upsell_option}" del upsell')
def step_impl(context, upsell_option):
    upsell_option = upsell_option.lower()
    if upsell_option == "mas costosa":
        context.currentPage.choose_max_price_upsell_option()

@Then('Click en botón seguir')
def step_impl(context):
    page = air_details(context)
    page.click_button_upsell_continue()
    context.currentPage = page
