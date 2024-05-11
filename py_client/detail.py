import requests

#get Inst
endpoint = "http://localhost:8000/api/1"
resp = requests.get(endpoint)
print(resp.json())