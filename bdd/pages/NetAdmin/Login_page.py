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

    def open_netadmin(self, context, environment):
        extensions = behave_extensions(self.context)
        extensions.set_context_environment(self.context, environment)
        self.context.browser.get(self.context.netsuite_environment['url'])
