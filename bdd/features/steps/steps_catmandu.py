import time
from behave import *
from bdd.pages.catmandu.Car_Result_Page import car_result_page
from bdd.pages.catmandu.Extras_Result_Page import extras_result_page
from bdd.pages.catmandu.Hotel_Result_Page import hotel_result_page
from bdd.pages.catmandu.Air_Result_Page import air_result_page
from bdd.pages.catmandu.Passenger_page import Passenger_page
from bdd.pages.catmandu.Air_Details import air_details
from bdd.pages.catmandu.Seat_Map_page import seat_map_page


@Given("Hacer búsqueda de hoteles en catmandu para ocupación {occupancy:w} para destino iata {destination:w}"
       " con fecha de checkin en {check_future_days:d} días y checkout en {check_out_future_days:d} días")
def step_impl(context, occupancy, destination, check_future_days, check_out_future_days):
    page = hotel_result_page(context)
    page.search_hotel(city=destination, check_future_days=check_future_days, check_out_future_days=check_out_future_days
                      , occupancy=occupancy)
    context.current_page = page


@When("Esperar que la página de resultados traiga hoteles en catmandú")
def step_impl(context):
    context.current_page.wait_results_hotel()


@When("Quitar filtro de solo hoteles con imagenes")
def step_impl(context):
    context.current_page.delete_filter_hoteles()

@When("Seleccionar la primera opción de hotel")
def step_impl(context):
    context.current_page.click_option_hotel()


@When("Seleccionar la opción {roomOption:d} del hotel {hotelOption:d} de la página de resultados de catmandú")
def step_impl(context, hotelOption, roomOption):
    if hotelOption >= 1:
        hotelOption = hotelOption - 1
    if roomOption >= 1:
        roomOption = roomOption-1
    page = hotel_result_page(context)
    page.obtained_hotel_price(context, hotelOption, roomOption)
    page.click_hotel_option_dinamic(hotelOption, roomOption)


@When("Esperar la página de pasajeros")
def step_impl(context):
    context.currentPage = Passenger_page(context)
    context.currentPage.wait_for_passenger_page()


@When("Esperar la validación de precios en página de pasajeros de catmandú")
def step_impl(context):
    context.currentPage.wait_until_price_validation()


@When("Llenar formulario de pasajeros")
def step_impl(context):
    context.currentPage.fill_passenger_information()

@Then("Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de air")
def step_impl(context):
    context.currentPage.obteined_passenger_price()
    context.currentPage.validation_air_price_passenger()


@Then("Validar que el precio en la pagina de hoteles sea el mismo precio que en pagina de pasajeros")
def step_impl(context):
    context.currentPage.obteined_passenger_price()
    context.currentPage.validation_price_passenger()


@When("Click botón continuar en página de pasajeros")
def step_impl(context):
    context.currentPage.click_button_continue()


@Given('Hacer búsqueda de aéreo en catmandu {airTripType:w} con la aerolinea {airLineCode:w} para ocupación {passengersCombination:w} saliendo desde {airCityFrom:w} con destino {airCityTo:w} con fecha de salida en {airDepartureFutureDays:d} días')
def step_impl(context, airTripType, airLineCode, passengersCombination, airCityFrom, airCityTo, airDepartureFutureDays):

    page = air_result_page(context)
    page.search_air(airTripType=airTripType, passengersCombination=passengersCombination, airCityFrom=airCityFrom,
                    airCityTo=airCityTo, airDepartureFutureDays=airDepartureFutureDays,airReturnFutureDays=None,
                    airLineCode=airLineCode)
    context.current_page = page


@When("Esperar que la página de resultados traiga aéreos en catmandú")
def step_impl(context):
    context.current_page.wait_results_air()


@When("Seleccionar la primera opción con upsell")
def step_impl(context):
    context.current_page.click_with_upsell_enabled()


@When("Esperar que la página de upsell se visualice en catmandu")
def step_impl(context):
    page = air_details(context)
    page.wait_results_upsell()
    context.currentPage = page


@When('Seleccionar la opción "{upsell_option}" del upsell')
def step_impl(context, upsell_option):
    upsell_option = upsell_option.lower()
    if upsell_option == "mas costosa":
        context.currentPage.choose_max_price_upsell_option()
        page = air_details(context)
        page.obteined_air_price()



@When("Click en botón seguir")
def step_impl(context):
    page = air_details(context)
    page.click_button_upsell_continue()
    context.currentPage = page

@When('Esperar que la pagina de productos de catmandu cargue en su totalidad')
def step_impl(context):
    page = extras_result_page(context)
    page.wait_product_view()

@When('Hacer click en el boton comprar ahora de la pagina de aereos con crosselling de catmandu')
def step_impl(context):
    """page = extra_product_page(context)
    page.click_button_purchase()
"""
@When("Dar click en el botón seleccionar sillas en la página de pasajeros de catmandú")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.currentPage.ClickOnSeatMapButton()

@When("Esperar hasta que se muestre el mapa de sillas en la página de selección de sillas de catmandú")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = seat_map_page(context)
    page.WaitUntilSeatmapIsShown()
    context.currentPage = page


@given('Hacer búsqueda de vuelo {airTripType:w} en la aerolínea {airLineCode:w} en catmandu para {passengersCombination:w} saliendo de {airCityFrom:w} con destino {airCityTo:w} con fecha de checkin en {airDepartureFutureDays:d} dias y checkout en {airReturnFutureDays:d} dias')
def step_impl(context, airTripType, airLineCode, passengersCombination, airCityFrom, airCityTo, airDepartureFutureDays,airReturnFutureDays):
    """
    :type context: behave.runner.Context
    """
    if airLineCode.lower() == 'cualquiera' or airLineCode.lower() == 'cualesquiera' or airLineCode.lower() == 'any':
        airLineCode = None

    page = air_result_page(context)
    page.search_air(airTripType=airTripType, passengersCombination=passengersCombination, airCityFrom=airCityFrom,
                      airCityTo=airCityTo, airDepartureFutureDays=airDepartureFutureDays, airReturnFutureDays=airReturnFutureDays,
                      airLineCode=airLineCode)
    context.currentPage = page

@When("Esperar que la página de resultados traiga vuelos en catmandú")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.currentPage.wait_results_air()

@When("Seleccionar la opción de vuelo que tenga habilitado upsell de la página de resultados de catmandú")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.currentPage = air_details(context)
    context.currentPage.click_onFlight_option_with_upsell_enabled()


@When("Esperar a que se muestre la página de detalles de vuelo en catmandú")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = air_details(context)
    page.wait_for_upsell_options()
    context.currentPage = page

@given("Hacer búsqueda de extras en {extra_city_from:w} con fecha desde en {extra_start_future_days:d}"
       " días y fecha hasta en {extra_end_future_days:d} días y ocupacion {occupancy:w}")
def step_impl(context, extra_city_from, extra_start_future_days, extra_end_future_days, occupancy):
    page = extras_result_page(context)
    page.search_extra(extra_city_from=extra_city_from, extra_start_future_days=extra_start_future_days,
                      extra_end_future_days=extra_end_future_days, occupancy=occupancy)
    context.current_page = page


@When('Esperar que la página de resultados traiga extras en catmandú')
def step_impl(context):
    context.current_page.wait_extra_results()


@When('Seleccionar la opción de extra {option:d} de la página de resultados de extras de catmandú')
def step_impl(context, option):
    context.current_page.select_option_extra(option)


@When('Esperar que la pagina de extras de catmandu cargue en su totalidad')
def step_impl(context):
    context.current_page.wait_product_view()
    context.current_page.obteined_extras_price()


@When('Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu')
def step_impl(context):
    context.current_page.load_quantity_person()


@When("Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu")
def step_impl(context):
    context.current_page.click_button_purchase()


@When("Esperar a que se muestre la pagina de pasajeros en catmandú")
def step_impl(context):
    context.currentPage = Passenger_page(context)
    context.currentPage.wait_until_price_validation()
    context.currentPage.wait_for_passenger_page()


@When('Llenar formulario de pasajero de extras en la página de pasajeros de catmandú')
def step_impl(context):
    context.currentPage.fill_passenger_information()


@Then("Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras")
def step_impl(context):
    context.currentPage.obteined_passenger_price()
    context.currentPage.validation_extra_price_passenger()


@When("Dar click en el botón continuar en la página de pasajeros de catmandú")
def step_impl(context):
    context.currentPage.click_button_continue()


@given("Hacer búsqueda de auto en {car_city_from:w} con fecha desde en {car_pickup_future_days:d}"
       " días y fecha hasta en {car_delivery_future_days:d} días")
def step_impl(context, car_city_from, car_pickup_future_days, car_delivery_future_days):
    page = car_result_page(context)
    page.search_car(car_city_from=car_city_from, car_pickup_future_days=car_pickup_future_days,
                    car_delivery_future_days=car_delivery_future_days)
    context.current_page = page


@When("Esperar que la página de resultados traiga autos en catmandú")
def step_impl(context):
    context.current_page.wait_car_results()


@When('Seleccionar la opción de auto {option:d} de la página de resultados de catmandú')
def step_impl(context, option):
    context.current_page.select_option_car(option)

@When('Esperar a que se muestre la página de detalles de auto en catmandú')
def step_impl(context):
    context.current_page.wait_car_product_view()

@When('Hacer click en la opcion del radio button pagar ahora de la pagina de detalle en catmandu')
def step_impl(context):
    context.current_page.select_radio_pay()
    context.current_page.obteined_car_price()


@When('Continuar de la pagina de detalles de auto de catmandu a la pagina de pago')
def step_impl(context):
    context.current_page.continue_button_click()

@When("Llenar formulario de conductor en la página de pasajeros de catmandú")
def step_impl(context):
    context.currentPage.obteined_passenger_price()
    context.currentPage.fill_passenger_information()



@Then("Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de car")
def step_impl(context):
    context.currentPage.validation_car_price_passenger()



