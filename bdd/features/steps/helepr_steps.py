from behave import *
import time


@When("Esperar {secs:d} segundos")
def step_impl(context, secs):
    """

    :param context:
    :param secs:
    :return:
    """
    time.sleep(secs)


