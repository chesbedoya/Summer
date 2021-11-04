from behave import use_fixture
from bdd.fixtures.fixtures import *
from behave.model import Scenario


def close_browser(context):
    if hasattr(context, 'browser'):
        if hasattr(context, 'close_browser'):
            if context.close_browser:
                context.browser.quit()


def before_tag(context, tag):
    if tag == "use.chrome.browser":
        use_fixture(use_chrome_browser, context)

    if tag == "close.browser":
        context.close_browser = True

    if tag == "preprod.regresion.es-CO.expedia":
        use_fixture(init_environment, context, environment='preprod', userService='regresion', language='es-CO',
                    sucursal='nuevaex')


def before_all(context):
    user_data = context.config.userdata
    continue_after_failed = user_data.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed
