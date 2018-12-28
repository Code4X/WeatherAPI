import json
import urllib.parse
import urllib.request
while True:
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
    print("Type the city's name or QUIT to exit the API: ")
    city = input()

    if city == "QUIT":
        quit()

    apikey = "eff23449aa567003d4bbce7599690cc6"

    url = api_endpoint + "?q=" + city + "&appid=" + apikey

    response = urllib.request.urlopen(url)
    parseResponse = json.loads(response.read())

    temperature = parseResponse['main']['temp']
    weather = parseResponse['weather'][0]['description']

    print(temperature)
    print(weather)


