from behave import *
from selenium.webdriver.support.ui import WebDriverWait
import time
from bdd.pages.NetAdmin.Login_page import Login_page
from bdd.pages.NetAdmin.Netadmin_page import Netadmin_page

@Then('Ingresar a netadmin ambiente {enviroment:w}')
def step_imp(context, enviroment):
    page = Login_page(context)
    page.open_netadmin(context, enviroment)
    context.current_page = page


@Then('Esperar que se muestre página de login de netadmin')
def step_imp(context):
    context.current_page.wait_netadmin_page()


@Then('Ingresar credenciales de login ambiente {enviroment:w}')
def step_imp(context, enviroment):
    if enviroment == 'testing':
        context.current_page.insert_credentials()


@Then('Hacer click en el boton ingresar')
def step_imp(context):
    context.current_page.click_button_login()


@Then('Ingresar itinerario en el buscador')
def step_imp(context):
    page = Netadmin_page(context)
    context.current_page = page
    context.current_page.insert_itinerary_number_in_netadmin()


@Then('Hacer click en el boton search')
def step_imp(context):
    context.current_page.click_button_search()


@Then('Hacer click en el boton cancelar')
def step_imp(context):
    context.current_page.wait_button_comments()
    context.current_page.wait_button_cancel_itinerary()