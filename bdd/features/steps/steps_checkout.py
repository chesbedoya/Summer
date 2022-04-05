from behave import *
from bdd.pages.NFF.Checkout import Checkout
from bdd.pages.NFF.Payment_page import Payment_page


@When("Esperar que se muestre la página de checkout")
def step_impl(context):
    context.currentPage = Checkout(context)
    context.currentPage.wait_checkout_page()


@When('Realizar pago con método de pago "{payment_form}" en página de checkout')
def step_impl(context, payment_form):
    pay_page = Checkout(context)
    if payment_form.lower() == 'tarjeta de crédito':
        context.currentPage.click_credit_card_payment_form()
        context.currentPage.fill_credit_card(context)
        context.currentPage.fill_geography_information()
        context.currentPage.obteined_checkout_price()
        context.currentPage.click_button_payment()
    elif payment_form.lower() == 'pago en agencia':
        context.currentPage.click_agency_payment_form()
        context.currentPage.fill_agency_payment(context)
        context.currentPage.fill_geography_information()
        context.currentPage.obteined_checkout_price()
        context.currentPage.click_button_payment_cash()
    elif payment_form.lower() == 'linea de credito':
        context.currentPage.click_credit_line_form()
        context.currentPage.fill_agency_payment(context)
        context.currentPage.fill_geography_information()
        context.currentPage.obteined_checkout_price()
        context.currentPage.click_button_payment_LOC()



@Then("Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout")
def step_impl(context):
    context.currentPage.validation_price_checkout()


@When('Esperar y dar click en ver itinerario')
def step_impl(context):
    context.currentPage = Payment_page(context)
    context.currentPage.wait_process_payment()
    context.currentPage.wait_display_page()


@Then('Validar que la reserva tenga estado confirmado')
def step_impl(context):
    context.currentPage.get_status_reservation()


