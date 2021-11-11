from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


def use_chrome_browser(context, **kwargs):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.chrome_session_id = context.browser.session_id


def create_base_url(context):
    if context.environment.lower() == 'preprod':
        return f"https://preprod.netactica.com"

    if context.environment.lower() == 'testing':
        return f"https://testing.netactica.com"


def init_environment(context, **kwargs):
    context.datetime = datetime.utcnow().strftime('%Y-%m-%d %H%M%S.%f')

    if 'environment' in kwargs:
        context.environment = kwargs['environment']

    if 'userService' in kwargs:
        context.userservice = kwargs['userService']

    if 'language' in kwargs:
        context.language = kwargs['language']

    if 'sucursal' in kwargs:
        context.sucursal = kwargs['sucursal']

    context.base_url = create_base_url(context)
