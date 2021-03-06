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

    if tag == "testing.regresiontest.es-CO.amadeus":
        use_fixture(init_environment, context, environment='testing', userService='regresiontest', language='es-CO',
                    sucursal='amadeus')

    if tag == "testing.regresiontest.es-CO.amadeusp2p":
        use_fixture(init_environment, context, environment='testing', userService='regresiontest', language='es-CO',
                    sucursal='amadeusp2p')

    if tag == "testing.regresiontest.es-CO.amdexchange":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="amdexchange")

    if tag == "testing.regresiontest.es-CO.amadeus_cabin":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="amd_cabine")

    if tag == "testing.regresiontest.es-CO.ApitudeExt":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="apitude_ex")

    if tag == "testing.regresiontest.es-CO.Omnitours":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="omnitours")

    if tag == "testing.regresiontest.es-CO.Omnibees":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="omnibees")

    if tag == "testing.regresiontest.es-CO.ResTel":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="restel")

    if tag == "testing.regresiontest.es-CO.Civitatis":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="civitatis")

    if tag == "testing.regresiontest.es-CO.RentingCarz":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="rentingcar")

    if tag == "testing.regresiontest.es-CO.localiza":
        use_fixture(init_environment, context, environment="testing", userService="regresiontest", language="es-CO",
                    sucursal="localiza")

def before_all(context):
    user_data = context.config.userdata
    continue_after_failed = user_data.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed
