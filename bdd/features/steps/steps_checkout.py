from behave import *
from bdd.pages.NFF.Checkout import Checkout


@Then("Esperar que se muestre la página de checkout")
def step_impl(context):
    context.currentPage = Checkout(context)
    context.currentPage.wait_checkout_page()


@Then('Realizar pago con método de pago "{payment_form}" en página de checkout')
def step_impl(context, payment_form):
    pay_page = Checkout(context)
    if payment_form.lower() == 'tarjeta de crédito':
        context.currentPage.click_credit_card_payment_form()
        context.currentPage.fill_credit_card(context)
