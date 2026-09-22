import requests

url = "https://google.com"

response = requests.get(url)

print(response.status_code)