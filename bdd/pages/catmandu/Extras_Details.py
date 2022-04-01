import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bdd.pages.BasePage import BasePage
from selenium.webdriver.support.ui import Select
class extras_details_page(BasePage):
    EXTRAS_INPUT_DATE = (By.ID, "date_1")
    EXTRAS_INPUT_ADULT = "ddl_Prod_0"
    EXTRAS_INPUT_CHILDREN = "ddl_Prod_1"
    EXTRAS_INPUT_INFANT = "ddl_Prod_2"
    EXTRAS_BUTTON_PURCHASE = (By.ID, "btnBuyNow_1")
    EXTRAS_BUTTON_CAR_PURCHASE = "btnPurchase_1"

    def __init__(self, context):
        BasePage.__init__(self, context)

    def wait_product_view(self):
        WebDriverWait(self.context.browser, 120).until(EC.visibility_of_element_located((By.ID, 'btnPurchase_1')))

    def obteined_extras_price(self):
        WebDriverWait(self.context.browser, 120) \
            .until(EC.visibility_of_element_located((By.XPATH,
                                                     "//div[@class='reprice header']//div[@class='currencyText price-extra money']//span[@class='currencyText']")))
        extras_price = self.context.browser.find_elements_by_xpath(
            "//div[@class='reprice header']//div[@class='currencyText price-extra money']//span[@class='currencyText']")
        price_result_extras = extras_price[0].text
        price_result_extras_replace = price_result_extras.replace("$ ", "").replace(".", "")
        price_extras_float_results = float(price_result_extras_replace)
        self.context.extras_price_options = price_extras_float_results
        return self.context.extras_price_options

    def load_quantity_person(self):
        WebDriverWait(self.context.browser, 30).until(
            EC.visibility_of_element_located((By.ID, 'ddl_Prod_0')))
        Select(self.context.browser.find_element_by_id('ddl_Prod_0')).select_by_value("1")

    def click_button_purchase(self):
        self.context.browser.execute_script(
            "return purchaseItems(false, 1, true)")


