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

    def wait_netadmin_page(self):
        WebDriverWait(self.context.browser, 60).until(EC.element_to_be_clickable
                                                      ((By.XPATH, "//div[@class='nts-row-buttons']/input")))

    def insert_credentials(self):
        WebDriverWait(self.context.browser, 40).until(EC.element_to_be_clickable
                                                      ((By.ID, "Login_UserName"))).send_keys('admin')

        WebDriverWait(self.context.browser, 40).until(EC.element_to_be_clickable
                                                      ((By.ID, "Login_Password"))).send_keys('mrbean')

        WebDriverWait(self.context.browser, 40).until(EC.element_to_be_clickable
                                                      ((By.ID, "Login_UserService"))).send_keys('regresiontest')

    def click_button_login(self):
        element = WebDriverWait(self.context.browser, 40).until(EC.element_to_be_clickable
                                                      ((By.XPATH, "//div[@id='Options']/input[@id='Login_btnLogin']")))

        element.click()

