import requests
from pprint import pprint

resp_msg = requests.get("https://jsonplaceholder.typicode.com/user/10")

if resp_msg.status_code == 200:
  print("Response:",resp_msg.status_code, '🎉🎉🎉', '\n')
else:
  print("Uh Oh, got",resp_msg.status_code)

dict = resp_msg.json()

print("name")
print("Email:")
print("city:")