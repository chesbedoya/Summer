from behave import use_fixture
from bdd.fixtures.fixtures import *
from behave.model import Scenario


def close_browser(context):
    if hasattr(context, 'browser'):
        if hasattr(context, 'close_browser'):
            if context.close_browser:
                context.browser.quit()


def after_scenario(context, scenario):
    close_browser(context)


def before_tag(context, tag):
    if tag == "use.chrome.browser":
        use_fixture(use_chrome_browser, context)

    if tag == "close.browser":
        context.close_browser = True

    if tag == "testing.simulacion.es-CO":
        use_fixture(init_environment, context, environment='testing', userService='simulacion', language='es-CO',
                    sucursal=None)

    if tag == "testing.palomalo.es-CO":
        use_fixture(init_environment, context, environment='testing', userService='palomalo', language='es-CO',
                    sucursal=None)

    if tag == "testing.regresiontest.es-CO.expedia":
        use_fixture(init_environment, context, environment='testing', userService='regresiontest', language='es-CO',
                    sucursal='hexp')

def before_all(context):
    user_data = context.config.userdata
    continue_after_failed = user_data.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed
