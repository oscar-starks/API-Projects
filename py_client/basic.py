import json
import requests

endpoint = "https://httpbin.org/anything"
endpoint = 'http://127.0.0.1:8000/test/detail/'
response = requests.get(endpoint, json={'name':'Oscar'})
# print(response.headers) 
print("---------")
print(response.json())
print("------------------")
# print(response.status_code)