import random
import requests
import json
import bdd.config.global_configuration as gc


class Mockaroo_request:

    def post_request(self, schema, num_rows_to_generate):
        try:
            url = gc.MOCKAROO_URL + '?key=' + gc.MOCKAROO_KEY + '&count=' + str(num_rows_to_generate) + '&schema=' + schema
            response = requests.post(url)
            json_response = json.loads(response.content)
            return json_response
        except Exception as e:
            print("Error al conectar con el api de Mockaroo " + str(e))

    def get_information_passenger_data(self):
        return self.post_request('Schema000001', '1')

    def get_document_passenger(self):
        return str(random.randint(1000000, 2000000))

    def get_payment_data(self):
        return self.post_request('Schema000003', '1')


