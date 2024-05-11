import requests

endpoint = "http://localhost:8000/api/instituition/"

resp = requests.post(endpoint, json={"name":"SJSU","state":"California","country":"USA"})
print(resp.json())