import json
import requests
from requests.auth import HTTPBasicAuth

endpoint = "https://httpbin.org/anything"
endpoint = 'http://localhost:8000/hotels/'
payload = {
        "duration_of_stay": 3,
        "signing_in_on": "2022-10-15",
        "signing_out_on": "2022-10-18",
        "email": "oscarblessred4@gmail.com",
        "price": 44,
        "hotel": 2
    }
response = requests.post(endpoint, data = payload, auth = HTTPBasicAuth('oscar', 'oscarblessed'))
# print(response.headers) 
print("---------")
print(response.json())
# val = response.json()
# print(val[0]["len_name"])
print("------------------")
# print(response.status_code)