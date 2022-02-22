from bdd.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.Extensions.behave_extensions import behave_extensions
from datetime import datetime
import time

class Login_page(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    def open_netadmin(self, context, enviroment):
        extensions = behave_extensions(self.context)
        extensions.set_context_enviroment(self.context, enviroment)
        self.context.browser.get(self.context.netsuite_enviroment['url'])
        context.datetime = datetime.now()
        time.sleep(100)