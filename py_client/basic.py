import json
import requests

endpoint = "https://httpbin.org/anything"
endpoint = 'http://localhost:8000/hotels/'
payload = {
    
    "duration_of_stay": 8,
    "signing_in_on": "2022-10-11",
    "signing_out_on": "2022-10-19",
    "email": "oscarblesserd04@gmail.com",
    "price": 45,
    "hotel": 2
}
response = requests.post(endpoint, data = payload)
# print(response.headers) 
print("---------")
print(response.json())
# val = response.json()
# print(val[0]["len_name"])
print("------------------")
# print(response.status_code)