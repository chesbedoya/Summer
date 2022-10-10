from behave import use_fixture
from bdd.fixtures.fixtures import *
from behave.model import Scenario
from bdd.Helpers.report_automation import prueba
from bdd.Helpers.jesikeiron_dic import var



def close_browser(context):
    if hasattr(context, 'browser'):
        if hasattr(context, 'close_browser'):
            if context.close_browser:
                context.browser.quit()


def after_scenario(context, scenario):
    close_browser(context)


def after_step(context, step):
    suripanto = prueba(context=context, step=step)
    print(suripanto)


def tag_in_list(list, tag):
    print(list,tag)
    for i in range(len(list)):
      if tag in list[i].values():
        return True, list[i]
    return False, {}


def before_tag(context, tag):
    if tag == "use.chrome.browser":
        use_fixture(use_chrome_browser, context)

    if tag == "use_appi_chrome_demo":
        use_fixture(use_appi_chrome_demo, context)

    if tag == "close.browser":
        context.close_browser = True

    flag, temp_dict = tag_in_list(var, tag)
    print(flag, temp_dict)
    if flag:
        use_fixture(init_environment, context, environment=temp_dict['environment'],
                    userService=temp_dict['userService'], language=temp_dict['language'],
                    sucursal=temp_dict['sucursal'])


def before_all(context):
    user_data = context.config.userdata
    print(user_data)
    continue_after_failed = user_data.getbool("runner.continue_after_failed_step", False)
    print(continue_after_failed)
    Scenario.continue_after_failed_step = continue_after_failed
