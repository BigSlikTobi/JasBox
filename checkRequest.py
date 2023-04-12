import requests

response = requests.get('http://localhost:5000/devices')
print(response.content)