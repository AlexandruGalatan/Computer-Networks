import requests
import json

number = 10

url = 'http://rt1:8001/post'

headers = {'Content-Type': 'application/json'}
data = {
    'value': number
}

response = requests.post(url, headers = headers, data = json.dumps(data))
responseData = response.json()

print(str(number) + '^2 = ' + str(responseData['squared_value']))
