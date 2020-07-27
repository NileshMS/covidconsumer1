import json
from covidconsumer1.settings import COVID_19_FILE
import requests


class CovidMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        response = requests.get('https://api.covid19india.org/state_district_wise.json')
        dict_data = json.loads(response.text)
        json.dump(dict_data, open(COVID_19_FILE, 'w'))

    def __call__(self, request, *arg, **kwargs):
        response = self.get_response(request)
        return response

