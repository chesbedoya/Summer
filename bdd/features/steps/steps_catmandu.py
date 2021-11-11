import time
from behave import *
from bdd.pages.catmandu.Hotel_Result_Page import hotel_result_page


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

