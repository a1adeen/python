# request module
import requests

# print(dir(requests))

response = requests.get("https://github.com/a1adeen")
print(response.text)