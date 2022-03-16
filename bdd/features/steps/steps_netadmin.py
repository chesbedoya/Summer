from behave import *
from bdd.pages.NetAdmin.Login_page import Login_page
from bdd.pages.NetAdmin.Netadmin_page import Netadmin_page
from bdd.Extensions.behave_extensions import behave_extensions
import time


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


@Then('Esperar que la pagina de Netadmin cargue')
def step_imp(context):
    page = Netadmin_page(context)
    context.current_page = page
    page.wait_loading_netadmin()
    page.wait_page_netadmin()


@Then('Ingresar itinerario y buscarlo en Netadmin')
def step_imp(context):
    page = Netadmin_page(context)
    context.current_page = page
    context.current_page.insert_itinerary_number_in_netadmin()


@Then('Hacer click en el boton cancelar')
def step_imp(context):
    page = Netadmin_page(context)
    ext = behave_extensions(context)
    ext.iframe_tab_netadmin()
    ext.iframe_display()
    page.wait_button_comments()
    #context.current_page.wait_button_cancel_itinerary()