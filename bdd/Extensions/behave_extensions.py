from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from bdd.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class behave_extensions(BasePage):

    def __int__(self, context):
        BasePage.__init__(self, context)

    def switch_to_frame_by_id_tokenex_number_card(self,
                                                  iframe_id='tx_iframe_ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl01_divTxtCardNumber'):
        """Este método se utiliza para cambiar de frame por el id del frame
        :param ïframe_id:¨id dentro del html

        """
        try:
            iframeElement = self.context.browser.find_element_by_id(iframe_id)
            self.context.browser.switch_to.frame(iframeElement)
        except:
            raise Exception("SwitchToFrameByNumber() Hubo una excepción en el flujo")

    def switch_to_frame_by_id_tokenex_code_card(self, iframe_id='tx_iframe_cvv_ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ctl01_divTxtCardCode'):
        """Este método se utiliza para cambiar de frame por el id del frame
        :param ïframe_id:¨id dentro del html

        """
        try:
            iframeElement = self.context.browser.find_element_by_id(iframe_id)
            self.context.browser.switch_to.frame(iframeElement)
        except:
            raise Exception("SwitchToFrameByNumber() Hubo una excepción en el flujo")

    def set_context_environment(self, context, environment):
        if environment == 'testing':
            self.context.netsuite_environment = {
                'url': 'https://testing.netactica.com/',
                'default_language': 'es-CO'
            }
