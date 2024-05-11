import requests

# delete instance
student_id = int(input("Enter Student ID to delete"))
endpoint = f"http://localhost:8000/api/student/{student_id}/delete/"
resp = requests.delete(endpoint)
print( resp.status_code, resp.status_code==204)