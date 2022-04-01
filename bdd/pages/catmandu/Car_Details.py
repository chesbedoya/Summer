import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage


class car_detail_page(BasePage):
    CAR_DETAIL_CONTINUE_BUTTON = (By.XPATH, "//div[@class='row collapse']//button[@class='button nts-button expanded small']")

    def __init__(self, context):
        BasePage.__init__(self, context=context)

    def wait_car_product_view(self):
        WebDriverWait(self.context.browser, 120).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='price-extra money']//span[@class='currencyText']")))

    def wait_for_continue_button(self):
        element = WebDriverWait(self.context.browser, 120)\
            .until(EC.visibility_of_element_located(self.CAR_DETAIL_CONTINUE_BUTTON))

    def wait_fot_processing(self):
        try:
            WebDriverWait(self.context.browser, 20) \
                .until(EC.presence_of_element_located((By.ID, "divProcessing")))

            WebDriverWait(self.context.browser, 20) \
                .until_not(EC.presence_of_element_located((By.ID, "divProcessing")))

        except TimeoutException:
            pass

    def obteined_car_price(self):
        WebDriverWait(self.context.browser, 120)\
        .until(EC.visibility_of_element_located((By.XPATH, "//div[@class='price-extra money']//span[@class='currencyText']")))
        car_price = self.context.browser.find_elements(
            By.XPATH, "//div[@class='price-extra money']//span[@class='currencyText']")
        price_result_car = car_price[0].text
        price_result_car_replace = price_result_car.replace("$ ", "").replace(".", "")
        price_car_float_results = float(price_result_car_replace)
        self.context.car_price_options = price_car_float_results
        return self.context.car_price_options

    def select_radio_pay(self):
        self.context.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        pay_now = self.context.browser.find_elements(By.XPATH,
                                                     "//div[@class='carRatePayNow show-for-large']//input[@name='chkRate']")

        pay_now_length = len(pay_now)
        if pay_now_length == 0:
            pass
        else:
            pay_now[0].click()


    def continue_button_click(self):
        script = 'return VehicleController.selectCarRate()'
        click_button = self.context.browser.execute_script(script)