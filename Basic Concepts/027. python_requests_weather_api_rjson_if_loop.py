import requests # Requires installation of requests library

r = requests.get('http://spartacodingclub.shop/en/global_air/seoul')
rjson = r.json()
# Converts the response to a JSON object into a python dictionary
days = rjson['data']['forecast']

for day in days:
    if day['avg']<100:
        print(day['day'], day['avg'])