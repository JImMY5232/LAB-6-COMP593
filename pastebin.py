import requests

resp_msg = requests.head('https://jsonplaceholder.typicode.com')

if resp_msg.status_code == 200:
  print('Response:',resp_msg.status, '🎉🎉🎉', '\n')
else:
  print('Uh Oh, got',resp_msg.status)

print(resp_msg.headers)