import requests
import json

url = "https://community-open-weather-map.p.rapidapi.com/weather"

sehir = input("sehrinizi girin: ")

querystring = {"q":""+sehir+",tr","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"tr","units":"metric","mode":"JSON"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "f814258b66msh49861db093fe599p1632dcjsnbae8b2297e91"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#removed = response.text.replace("test(","") == "test(" i çıkarıyor
#removed = response.text[5:] ilk beş karakteri çıkarıyor
removed = response.text[5:-1]
print(removed)
y = json.loads(removed)
print(y['main']['temp'])

#response.text = {"coord":{"lon":27.0923,"lat":38.4622},"weather":[{"id":800,"main":"Clear","description":"açık","icon":"01d"}],"base":"stations","main":{"temp":17.92,"feelslike":17.02,"tempmin":17.58,"temp_max":17.97,"pressure":1017,"humidity":48},"visibility":10000,"wind":{"speed":0,"deg":0},"clouds":{"all":0},"dt":1637073331,"sys":{"type":1,"id":6979,"country":"TR","sunrise":1637038471,"sunset":1637074713},"timezone":10800,"id":311044,"name":"İzmir","cod":200}
