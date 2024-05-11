import requests

#get all Inst
endpoint = "http://localhost:8000/api/"
resp = requests.get(endpoint)
print(resp.json())