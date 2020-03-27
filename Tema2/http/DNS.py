#program that prints the IP of a given website using cloudflare-dns.com

import requests
import json

searchAddress = 'fmi.unibuc.ro'

requestHeader = {
    'accept': 'application/dns-json'
}

def getIP(address):
    requestParameters = {
        "name": address,
        "type": "A"
    }

    response = requests.get('https://1.1.1.1/dns-query', headers=requestHeader, params = requestParameters)

    responseJSON = json.loads(response.text)
    IP = responseJSON['Answer'][0]['data']

    return IP

print(searchAddress + ": " + getIP(searchAddress))
