import requests

#get all Inst
data = {
    "name": "revii",
    "email_id": "revii@gmail.com",
    "instituition": 2
}
endpoint = "http://localhost:8000/api/student/2/update/"
resp = requests.put(endpoint, json=data)
print(resp.json())