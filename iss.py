import requests
import json
import os

URL = 'http://api.open-notify.org/iss-now.json'

response = requests.get(URL)
iss = json.loads(response.text)

iss_latitude = iss['iss_position']['latitude']
iss_longitude = iss['iss_position']['longitude']

print("# HELP ISS latitude\n# TYPE ISS latitude\n" "ISS_latitude " + iss_latitude)
print("# HELP ISS longitud\n# TYPE ISS longitud\n" "ISS_longitud " + iss_longitude)