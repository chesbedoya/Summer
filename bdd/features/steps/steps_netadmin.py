from behave import *
from selenium.webdriver.support.ui import WebDriverWait
import time
from bdd.pages.NetAdmin.Login_page import Login_page


@Then ('Ingresar a netadmin ambiente {enviroment:w}')
def step_imp(context, enviroment):
    page = Login_page(context)
    page.open_netadmin(context, enviroment)