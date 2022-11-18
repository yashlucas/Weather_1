from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=acdcd16aa789873f5c107084399920f5'

    city = 'Hyderabad'
    city2= 'Pune'
    city3= 'Chennai'
    city4= 'Mumbai'
    city5= 'Delhi'

    city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
    city_weather2 = requests.get(url.format(city2)).json()
    city_weather3 = requests.get(url.format(city3)).json()
    city_weather4 = requests.get(url.format(city4)).json()
    city_weather5 = requests.get(url.format(city5)).json()
    print(city_weather) #checking the output
    weather = {
        'city' : city,
        'city2': city2,
        'temperature' : city_weather['main']['temp'],
        'temperature2' : city_weather2['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'description2' : city_weather2['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'icon2' : city_weather2['weather'][0]['icon'],
        'humidity': city_weather['main']['humidity'],
        'lon2': city_weather2['coord']['lon'],
        'wind': city_weather['wind']['speed'],
        'lat2': city_weather2['coord']['lat'],
        'city3': city3,
        'temperature3' : city_weather3['main']['temp'],
        'description3' : city_weather3['weather'][0]['description'],
        'icon3' : city_weather3['weather'][0]['icon'],
        'sunrise3': city_weather3['sys']['sunrise'],
        'sunset3': city_weather3['sys']['sunset'],
        'city4': city4,
        'temperature4' : city_weather4['main']['temp'],
        'description4' : city_weather4['weather'][0]['description'],
        'icon4' : city_weather4['weather'][0]['icon'],
        'min4': city_weather4['main']['temp_min'],
        'max4': city_weather4['main']['temp_max'],
        'city5': city5,
        'temperature5' : city_weather5['main']['temp'],
        'description5' : city_weather5['weather'][0]['description'],
        'icon5' : city_weather5['weather'][0]['icon'],
        'pressure5': city_weather5['main']['pressure'],
        'clouds5': city_weather5['clouds']['all']
        
    }

    

    return render(request, 'index.html', {'weather' : weather}) #returns the index.html template

    