from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from appium.webdriver.webdriver import WebDriver as AppiumDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver


def use_chrome_browser(context, **kwargs):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.chrome_session_id = context.browser.session_id


def use_appi_chrome_demo(context):
    appium_capabilities = {
        'automationName': 'Appium',
        'platformName': 'Android',
        'deviceName': 'Android',
        'app': 'APK_PATH'
    }
    context.appium = AppiumDriver(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities=appium_capabilities)

    context.browser = context.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version="102.0.5005.61").install()))

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
