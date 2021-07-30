
import datetime
import responses

import googlemaps
from . import TestCase


print("SOLICITANDO INFORMACIÓN DE UBICACIÓN CON RAPPI")
print("espere....")

class GeocodingTest(TestCase):
    def setUp(self):
        self.key = "AIzaasdf"
        self.client = googlemaps.Client(self.key)

print("Accediendo a la información dela tienda")
URL = 'https://microservices.dev.rappi.com/api/v2/restaurants-integrations-public-api/stores-pa'

data = requests.get(URL) 

data = data.json() #convertimos la respuesta en dict
print(data)
print(data.status_code)
for element in data: #iteramos sobre data
    print(len(element)) #Accedemos a sus valores

print("Accediendo a la ubicación cerca de la tienda con google maps")
@responses.activate
def test_reverse_geocode(self):
    responses.add(
        responses.GET,
        "https://maps.googleapis.com/maps/api/geocode/json",
        body='{"status":"OK","results":[]}',
        status=200,
        content_type="application/json",
    )

    results = self.client.reverse_geocode((-33.8674869, 151.2069902))

    self.assertEqual(1, len(responses.calls))
    self.assertURLEqual(
        "https://maps.googleapis.com/maps/api/geocode/json?"
        "latlng=-33.8674869,151.2069902&key=%s" % self.key,
        responses.calls[0].request.url,
    )
